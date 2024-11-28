from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, status, generics
from .models import *
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken



User = get_user_model()

class RegistrationView(APIView):
    """
    Handles user registration.
    """
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({"error": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({"error": "Email is already registered."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(
            email=email,
            password=make_password(password),
            is_verified=False  # Assume verification is required
        )
        return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)


class AuthenticationView(APIView):
    """
    Handles user authentication and provides JWT tokens.
    """
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email)
            if not user.check_password(password):
                raise Exception("Invalid credentials")

            if not user.is_verified:
                return Response({"error": "User not verified."}, status=status.HTTP_401_UNAUTHORIZED)

            # Generate tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            })

        except User.DoesNotExist:
            return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)


class VerificationView(APIView):
    """
    Handles user verification.
    """
    def post(self, request):
        email = request.data.get('email')

        try:
            user = User.objects.get(email=email)
            if user.is_verified:
                return Response({"message": "User already verified."}, status=status.HTTP_200_OK)

            # Simulate verification (e.g., via email or token)
            user.is_verified = True
            user.save()
            return Response({"message": "User verified successfully."}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)


class CurrentUserView(APIView):
    """
    Returns the current user's information.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        return Response({
            "email": user.email,
            "is_verified": user.is_verified
        })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = request.user
    return Response({"email": user.email})

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD operations for categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CartViewSet(viewsets.ViewSet):
    """
    A ViewSet to handle Cart and Cart Items.
    """

    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        """
        Retrieve the user's cart and its items.
        """
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def create(self, request):
        """
        Add an item to the cart.
        """
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cart=cart)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        Retrieve a specific cart item by ID.
        """
        try:
            cart_item = CartItem.objects.get(pk=pk, cart__user=request.user)
            serializer = CartItemSerializer(cart_item)
            return Response(serializer.data)
        except CartItem.DoesNotExist:
            return Response({'detail': 'Cart item not found.'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """
        Update a cart item (e.g., quantity).
        """
        try:
            cart_item = CartItem.objects.get(pk=pk, cart__user=request.user)
            serializer = CartItemSerializer(cart_item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CartItem.DoesNotExist:
            return Response({'detail': 'Cart item not found.'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        """
        Remove an item from the cart.
        """
        try:
            cart_item = CartItem.objects.get(pk=pk, cart__user=request.user)
            cart_item.delete()
            return Response({'detail': 'Cart item removed.'}, status=status.HTTP_204_NO_CONTENT)
        except CartItem.DoesNotExist:
            return Response({'detail': 'Cart item not found.'}, status=status.HTTP_404_NOT_FOUND)
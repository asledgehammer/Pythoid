from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.nio import FloatBuffer

class Matrix:

  def determinant(self) -> float: ...

  def invert(self) -> Matrix: ...

  def load(self, arg0: FloatBuffer) -> Matrix: ...

  def loadTranspose(self, arg0: FloatBuffer) -> Matrix: ...

  def negate(self) -> Matrix: ...

  def setIdentity(self) -> Matrix: ...

  def setZero(self) -> Matrix: ...

  def store(self, arg0: FloatBuffer) -> Matrix: ...

  def storeTranspose(self, arg0: FloatBuffer) -> Matrix: ...

  def transpose(self) -> Matrix: ...


class Matrix2f(Matrix):

  def determinant(self) -> float: ...

  def invert(self) -> Matrix: ...

  @overload
  def load(self, arg0: FloatBuffer) -> Matrix: ...

  @overload
  def load(self, arg0: Matrix2f) -> Matrix2f: ...

  def loadTranspose(self, arg0: FloatBuffer) -> Matrix: ...

  @overload
  def negate(self) -> Matrix: ...

  @overload
  def negate(self, arg0: Matrix2f) -> Matrix2f: ...

  def setIdentity(self) -> Matrix: ...

  def setZero(self) -> Matrix: ...

  def store(self, arg0: FloatBuffer) -> Matrix: ...

  def storeTranspose(self, arg0: FloatBuffer) -> Matrix: ...

  def toString(self) -> str: ...

  @overload
  def transpose(self) -> Matrix: ...

  @overload
  def transpose(self, arg0: Matrix2f) -> Matrix2f: ...

  @staticmethod
  def add(arg0: Matrix2f, arg1: Matrix2f, arg2: Matrix2f) -> Matrix2f: ...

  @staticmethod
  def mul(arg0: Matrix2f, arg1: Matrix2f, arg2: Matrix2f) -> Matrix2f: ...

  @staticmethod
  def sub(arg0: Matrix2f, arg1: Matrix2f, arg2: Matrix2f) -> Matrix2f: ...

  @staticmethod
  def transform(arg0: Matrix2f, arg1: Vector2f, arg2: Vector2f) -> Vector2f: ...

  @overload
  def __init__(self):
    self.m00: float

    self.m01: float

    self.m10: float

    self.m11: float

  @overload
  def __init__(self, arg0: Matrix2f): ...


class Matrix3f(Matrix):

  def determinant(self) -> float: ...

  def invert(self) -> Matrix: ...

  @overload
  def load(self, arg0: FloatBuffer) -> Matrix: ...

  @overload
  def load(self, arg0: Matrix3f) -> Matrix3f: ...

  def loadTranspose(self, arg0: FloatBuffer) -> Matrix: ...

  @overload
  def negate(self) -> Matrix: ...

  @overload
  def negate(self, arg0: Matrix3f) -> Matrix3f: ...

  def setIdentity(self) -> Matrix: ...

  def setZero(self) -> Matrix: ...

  def store(self, arg0: FloatBuffer) -> Matrix: ...

  def storeTranspose(self, arg0: FloatBuffer) -> Matrix: ...

  def toString(self) -> str: ...

  @overload
  def transpose(self) -> Matrix: ...

  @overload
  def transpose(self, arg0: Matrix3f) -> Matrix3f: ...

  @staticmethod
  def add(arg0: Matrix3f, arg1: Matrix3f, arg2: Matrix3f) -> Matrix3f: ...

  @staticmethod
  def mul(arg0: Matrix3f, arg1: Matrix3f, arg2: Matrix3f) -> Matrix3f: ...

  @staticmethod
  def sub(arg0: Matrix3f, arg1: Matrix3f, arg2: Matrix3f) -> Matrix3f: ...

  @staticmethod
  def transform(arg0: Matrix3f, arg1: Vector3f, arg2: Vector3f) -> Vector3f: ...

  def __init__(self):
    self.m00: float
    self.m01: float
    self.m02: float
    self.m10: float
    self.m11: float
    self.m12: float
    self.m20: float
    self.m21: float
    self.m22: float


class Matrix4f(Matrix):

  def determinant(self) -> float: ...

  def invert(self) -> Matrix: ...

  @overload
  def load(self, arg0: FloatBuffer) -> Matrix: ...

  @overload
  def load(self, arg0: Matrix4f) -> Matrix4f: ...

  def loadTranspose(self, arg0: FloatBuffer) -> Matrix: ...

  @overload
  def negate(self) -> Matrix: ...

  @overload
  def negate(self, arg0: Matrix4f) -> Matrix4f: ...

  @overload
  def rotate(self, arg0: float, arg1: Vector3f) -> Matrix4f: ...

  @overload
  def rotate(self, arg0: float, arg1: Vector3f, arg2: Matrix4f) -> Matrix4f: ...

  def scale(self, arg0: Vector3f) -> Matrix4f: ...

  def setIdentity(self) -> Matrix: ...

  def setZero(self) -> Matrix: ...

  def store(self, arg0: FloatBuffer) -> Matrix: ...

  def store3f(self, arg0: FloatBuffer) -> Matrix: ...

  def storeTranspose(self, arg0: FloatBuffer) -> Matrix: ...

  def toString(self) -> str: ...

  @overload
  def translate(self, arg0: Vector2f) -> Matrix4f: ...

  @overload
  def translate(self, arg0: Vector3f) -> Matrix4f: ...

  @overload
  def translate(self, arg0: Vector2f, arg1: Matrix4f) -> Matrix4f: ...

  @overload
  def translate(self, arg0: Vector3f, arg1: Matrix4f) -> Matrix4f: ...

  @overload
  def transpose(self) -> Matrix: ...

  @overload
  def transpose(self, arg0: Matrix4f) -> Matrix4f: ...

  @staticmethod
  def add(arg0: Matrix4f, arg1: Matrix4f, arg2: Matrix4f) -> Matrix4f: ...

  @staticmethod
  def mul(arg0: Matrix4f, arg1: Matrix4f, arg2: Matrix4f) -> Matrix4f: ...

  @staticmethod
  def sub(arg0: Matrix4f, arg1: Matrix4f, arg2: Matrix4f) -> Matrix4f: ...

  @staticmethod
  def transform(arg0: Matrix4f, arg1: Vector4f, arg2: Vector4f) -> Vector4f: ...

  @overload
  def __init__(self):
    self.m00: float

    self.m01: float

    self.m02: float

    self.m03: float

    self.m10: float

    self.m11: float

    self.m12: float

    self.m13: float

    self.m20: float

    self.m21: float

    self.m22: float

    self.m23: float

    self.m30: float

    self.m31: float

    self.m32: float

    self.m33: float

  @overload
  def __init__(self, arg0: Matrix4f): ...


class Quaternion(Vector):

  @overload
  def getW(self) -> float: ...

  @overload
  def getW(self) -> float: ...

  def getX(self) -> float: ...

  def getY(self) -> float: ...

  def getZ(self) -> float: ...

  def lengthSquared(self) -> float: ...

  def load(self, arg0: FloatBuffer) -> Vector: ...

  @overload
  def negate(self) -> Vector: ...

  @overload
  def negate(self, arg0: Quaternion) -> Quaternion: ...

  def normalise(self, arg0: Quaternion) -> Quaternion: ...

  def scale(self, arg0: float) -> Vector: ...

  @overload
  def set(self, arg0: ReadableVector4f) -> Quaternion: ...

  @overload
  def set(self, arg0: float, arg1: float) -> None: ...

  @overload
  def set(self, arg0: float, arg1: float, arg2: float) -> None: ...

  @overload
  def set(self, arg0: float, arg1: float, arg2: float, arg3: float) -> None: ...

  def setFromAxisAngle(self, arg0: Vector4f) -> None: ...

  @overload
  def setFromMatrix(self, arg0: Matrix3f) -> Quaternion: ...

  @overload
  def setFromMatrix(self, arg0: Matrix4f) -> Quaternion: ...

  def setIdentity(self) -> Quaternion: ...

  def setW(self, arg0: float) -> None: ...

  def setX(self, arg0: float) -> None: ...

  def setY(self, arg0: float) -> None: ...

  def setZ(self, arg0: float) -> None: ...

  def store(self, arg0: FloatBuffer) -> Vector: ...

  def toString(self) -> str: ...

  @staticmethod
  def dot(arg0: Quaternion, arg1: Quaternion) -> float: ...

  @staticmethod
  def mul(arg0: Quaternion, arg1: Quaternion, arg2: Quaternion) -> Quaternion: ...

  @staticmethod
  def mulInverse(arg0: Quaternion, arg1: Quaternion, arg2: Quaternion) -> Quaternion: ...

  @overload
  def __init__(self):
    self.w: float

    self.x: float

    self.y: float

    self.z: float

  @overload
  def __init__(self, arg0: ReadableVector4f): ...
  @overload
  def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float): ...


class ReadableVector:

  def length(self) -> float: ...

  def lengthSquared(self) -> float: ...

  def store(self, arg0: FloatBuffer) -> Vector: ...


class ReadableVector2f:

  def getX(self) -> float: ...

  def getY(self) -> float: ...

  def length(self) -> float: ...

  def lengthSquared(self) -> float: ...

  def store(self, arg0: FloatBuffer) -> Vector: ...


class ReadableVector3f:

  def getX(self) -> float: ...

  def getY(self) -> float: ...

  def getZ(self) -> float: ...


class ReadableVector4f:

  def getW(self) -> float: ...

  def getZ(self) -> float: ...


class Vector:

  @overload
  def length(self) -> float: ...

  @overload
  def length(self) -> float: ...

  @overload
  def lengthSquared(self) -> float: ...

  @overload
  def lengthSquared(self) -> float: ...

  def load(self, arg0: FloatBuffer) -> Vector: ...

  def negate(self) -> Vector: ...

  def normalise(self) -> Vector: ...

  def scale(self, arg0: float) -> Vector: ...

  @overload
  def store(self, arg0: FloatBuffer) -> Vector: ...

  @overload
  def store(self, arg0: FloatBuffer) -> Vector: ...


class Vector2f(Vector):

  @overload
  def getX(self) -> float: ...

  @overload
  def getX(self) -> float: ...

  @overload
  def getY(self) -> float: ...

  @overload
  def getY(self) -> float: ...

  def lengthSquared(self) -> float: ...

  def load(self, arg0: FloatBuffer) -> Vector: ...

  @overload
  def negate(self) -> Vector: ...

  @overload
  def negate(self, arg0: Vector2f) -> Vector2f: ...

  def normalise(self, arg0: Vector2f) -> Vector2f: ...

  def scale(self, arg0: float) -> Vector: ...

  @overload
  def set(self, arg0: ReadableVector2f) -> Vector2f: ...

  @overload
  def set(self, arg0: float, arg1: float) -> None: ...

  @overload
  def set(self, arg0: float, arg1: float) -> None: ...

  @overload
  def setX(self, arg0: float) -> None: ...

  @overload
  def setX(self, arg0: float) -> None: ...

  @overload
  def setY(self, arg0: float) -> None: ...

  @overload
  def setY(self, arg0: float) -> None: ...

  def store(self, arg0: FloatBuffer) -> Vector: ...

  def toString(self) -> str: ...

  def translate(self, arg0: float, arg1: float) -> Vector2f: ...

  @staticmethod
  def add(arg0: Vector2f, arg1: Vector2f, arg2: Vector2f) -> Vector2f: ...

  @staticmethod
  def angle(arg0: Vector2f, arg1: Vector2f) -> float: ...

  @staticmethod
  def dot(arg0: Vector2f, arg1: Vector2f) -> float: ...

  @staticmethod
  def sub(arg0: Vector2f, arg1: Vector2f, arg2: Vector2f) -> Vector2f: ...

  @overload
  def __init__(self):
    self.x: float

    self.y: float

  @overload
  def __init__(self, arg0: ReadableVector2f): ...
  @overload
  def __init__(self, arg0: float, arg1: float): ...


class Vector3f(Vector):

  def getX(self) -> float: ...

  def getY(self) -> float: ...

  @overload
  def getZ(self) -> float: ...

  @overload
  def getZ(self) -> float: ...

  def lengthSquared(self) -> float: ...

  def load(self, arg0: FloatBuffer) -> Vector: ...

  @overload
  def negate(self) -> Vector: ...

  @overload
  def negate(self, arg0: Vector3f) -> Vector3f: ...

  def normalise(self, arg0: Vector3f) -> Vector3f: ...

  def scale(self, arg0: float) -> Vector: ...

  @overload
  def set(self, arg0: ReadableVector3f) -> Vector3f: ...

  @overload
  def set(self, arg0: float, arg1: float) -> None: ...

  @overload
  def set(self, arg0: float, arg1: float, arg2: float) -> None: ...

  @overload
  def set(self, arg0: float, arg1: float, arg2: float) -> None: ...

  def setX(self, arg0: float) -> None: ...

  def setY(self, arg0: float) -> None: ...

  @overload
  def setZ(self, arg0: float) -> None: ...

  @overload
  def setZ(self, arg0: float) -> None: ...

  def store(self, arg0: FloatBuffer) -> Vector: ...

  def toString(self) -> str: ...

  def translate(self, arg0: float, arg1: float, arg2: float) -> Vector3f: ...

  @staticmethod
  def add(arg0: Vector3f, arg1: Vector3f, arg2: Vector3f) -> Vector3f: ...

  @staticmethod
  def angle(arg0: Vector3f, arg1: Vector3f) -> float: ...

  @staticmethod
  def cross(arg0: Vector3f, arg1: Vector3f, arg2: Vector3f) -> Vector3f: ...

  @staticmethod
  def dot(arg0: Vector3f, arg1: Vector3f) -> float: ...

  @staticmethod
  def sub(arg0: Vector3f, arg1: Vector3f, arg2: Vector3f) -> Vector3f: ...

  @overload
  def __init__(self):
    self.x: float

    self.y: float

    self.z: float

  @overload
  def __init__(self, arg0: ReadableVector3f): ...
  @overload
  def __init__(self, arg0: float, arg1: float, arg2: float): ...


class Vector4f(Vector):

  @overload
  def getW(self) -> float: ...

  @overload
  def getW(self) -> float: ...

  def getX(self) -> float: ...

  def getY(self) -> float: ...

  def getZ(self) -> float: ...

  def lengthSquared(self) -> float: ...

  def load(self, arg0: FloatBuffer) -> Vector: ...

  @overload
  def negate(self) -> Vector: ...

  @overload
  def negate(self, arg0: Vector4f) -> Vector4f: ...

  def normalise(self, arg0: Vector4f) -> Vector4f: ...

  def scale(self, arg0: float) -> Vector: ...

  @overload
  def set(self, arg0: ReadableVector4f) -> Vector4f: ...

  @overload
  def set(self, arg0: float, arg1: float) -> None: ...

  @overload
  def set(self, arg0: float, arg1: float, arg2: float) -> None: ...

  @overload
  def set(self, arg0: float, arg1: float, arg2: float, arg3: float) -> None: ...

  @overload
  def set(self, arg0: float, arg1: float, arg2: float, arg3: float) -> None: ...

  @overload
  def setW(self, arg0: float) -> None: ...

  @overload
  def setW(self, arg0: float) -> None: ...

  def setX(self, arg0: float) -> None: ...

  def setY(self, arg0: float) -> None: ...

  def setZ(self, arg0: float) -> None: ...

  def store(self, arg0: FloatBuffer) -> Vector: ...

  def toString(self) -> str: ...

  def translate(self, arg0: float, arg1: float, arg2: float, arg3: float) -> Vector4f: ...

  @staticmethod
  def add(arg0: Vector4f, arg1: Vector4f, arg2: Vector4f) -> Vector4f: ...

  @staticmethod
  def angle(arg0: Vector4f, arg1: Vector4f) -> float: ...

  @staticmethod
  def dot(arg0: Vector4f, arg1: Vector4f) -> float: ...

  @staticmethod
  def sub(arg0: Vector4f, arg1: Vector4f, arg2: Vector4f) -> Vector4f: ...

  @overload
  def __init__(self):
    self.w: float

    self.x: float

    self.y: float

    self.z: float

  @overload
  def __init__(self, arg0: ReadableVector4f): ...
  @overload
  def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float): ...


class WritableVector2f:

  def set(self, arg0: float, arg1: float) -> None: ...

  def setX(self, arg0: float) -> None: ...

  def setY(self, arg0: float) -> None: ...


class WritableVector3f:

  @overload
  def set(self, arg0: float, arg1: float) -> None: ...

  @overload
  def set(self, arg0: float, arg1: float, arg2: float) -> None: ...

  def setX(self, arg0: float) -> None: ...

  def setY(self, arg0: float) -> None: ...

  def setZ(self, arg0: float) -> None: ...


class WritableVector4f:

  @overload
  def set(self, arg0: float, arg1: float, arg2: float) -> None: ...

  @overload
  def set(self, arg0: float, arg1: float, arg2: float, arg3: float) -> None: ...

  def setW(self, arg0: float) -> None: ...

  def setZ(self, arg0: float) -> None: ...

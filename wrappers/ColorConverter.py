import maglev
import colorconverter

from typing import Any, List, Callable

class ColorConverter:
	"""
	An Library for Color Conversion
	"""
	def __init__(self):
		bus = maglev.maglev_MagLev.getInstance("default")
		lib = colorconverter.colorconverter_ColorConverter(bus)

	def FromRGB(self, r: float, g: float, b: float) -> List[Any]:
		"""		Convert from RGB
		Args:
			r (float):
			g (float):
			b (float):
		Returns:
			
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = [r, g, b]
		ret = None
		def FromRGB_Ret(async_ret):
			nonlocal ret
			ret = async_ret
		pybus.call('ColorConverter.FromRGB', args, FromRGB_Ret)
		return ret

	def FromCIELAB(self, L: float, a: float, b: float) -> List[Any]:
		"""		Convert from CIELAB
		Args:
			L (float):
			a (float):
			b (float):
		Returns:
			
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = [L, a, b]
		ret = None
		def FromCIELAB_Ret(async_ret):
			nonlocal ret
			ret = async_ret
		pybus.call('ColorConverter.FromCIELAB', args, FromCIELAB_Ret)
		return ret

	def FromCMYK(self, c: float, m: float, y: float, k: float) -> List[Any]:
		"""		Convert from CMYK
		Args:
			c (float):
			m (float):
			y (float):
			k (float):
		Returns:
			
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = [c, m, y, k]
		ret = None
		def FromCMYK_Ret(async_ret):
			nonlocal ret
			ret = async_ret
		pybus.call('ColorConverter.FromCMYK', args, FromCMYK_Ret)
		return ret

	def FromHEX(self, hex: str) -> List[Any]:
		"""		Convert from HEX
		Args:
			hex (str):
		Returns:
			
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = [hex]
		ret = None
		def FromHEX_Ret(async_ret):
			nonlocal ret
			ret = async_ret
		pybus.call('ColorConverter.FromHEX', args, FromHEX_Ret)
		return ret

	def FromXYZ(self, x: float, y: float, z: float) -> List[Any]:
		"""		Convert from XYZ
		Args:
			x (float):
			y (float):
			z (float):
		Returns:
			
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = [x, y, z]
		ret = None
		def FromXYZ_Ret(async_ret):
			nonlocal ret
			ret = async_ret
		pybus.call('ColorConverter.FromXYZ', args, FromXYZ_Ret)
		return ret

	def ConvertRGB(self, r: float, g: float, b: float, observer1: str, observer2: str) -> List[Any]:
		"""		Convert from RGB using illumination and observer angles
		Args:
			r (float):
			g (float):
			b (float):
			observer1 (str):
			observer2 (str):
		Returns:
			
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = [r, g, b, observer1, observer2]
		ret = None
		def ConvertRGB_Ret(async_ret):
			nonlocal ret
			ret = async_ret
		pybus.call('ColorConverter.ConvertRGB', args, ConvertRGB_Ret)
		return ret

	def ConvertCIELAB(self, L: float, a: float, b: float, observer1: str, observer2: str) -> List[Any]:
		"""		Convert from CIELAB using illumination and observer angles
		Args:
			L (float):
			a (float):
			b (float):
			observer1 (str):
			observer2 (str):
		Returns:
			
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = [L, a, b, observer1, observer2]
		ret = None
		def ConvertCIELAB_Ret(async_ret):
			nonlocal ret
			ret = async_ret
		pybus.call('ColorConverter.ConvertCIELAB', args, ConvertCIELAB_Ret)
		return ret

	def ConvertCMYK(self, c: float, m: float, y: float, k: float, observer1: str, observer2: str) -> List[Any]:
		"""		Convert from CMYK using illumination and observer angles
		Args:
			c (float):
			m (float):
			y (float):
			k (float):
			observer1 (str):
			observer2 (str):
		Returns:
			
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = [c, m, y, k, observer1, observer2]
		ret = None
		def ConvertCMYK_Ret(async_ret):
			nonlocal ret
			ret = async_ret
		pybus.call('ColorConverter.ConvertCMYK', args, ConvertCMYK_Ret)
		return ret

	def ConvertHEX(self, hex: str, observer1: str, observer2: str) -> List[Any]:
		"""		Convert from HEX using illumination and observer angles
		Args:
			hex (str):
			observer1 (str):
			observer2 (str):
		Returns:
			
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = [hex, observer1, observer2]
		ret = None
		def ConvertHEX_Ret(async_ret):
			nonlocal ret
			ret = async_ret
		pybus.call('ColorConverter.ConvertHEX', args, ConvertHEX_Ret)
		return ret

	def ConvertXYZ(self, x: float, y: float, z: float, observer1: str, observer2: str) -> List[Any]:
		"""		Convert from XYZ using illumination and observer angles
		Args:
			x (float):
			y (float):
			z (float):
			observer1 (str):
			observer2 (str):
		Returns:
			
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = [x, y, z, observer1, observer2]
		ret = None
		def ConvertXYZ_Ret(async_ret):
			nonlocal ret
			ret = async_ret
		pybus.call('ColorConverter.ConvertXYZ', args, ConvertXYZ_Ret)
		return ret

	def AddReferenceColorByRGB(self, system: str, name: str, description: str, r: float, g: float, b: float):
		"""		Add a reference color
		Args:
			system (str):
			name (str):
			description (str):
			r (float):
			g (float):
			b (float):
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = [system, name, description, r, g, b]
		ret = None
		def AddReferenceColorByRGB_Ret(async_ret):
			nonlocal ret
			ret = async_ret
		pybus.call('ColorConverter.AddReferenceColorByRGB', args, AddReferenceColorByRGB_Ret)

	def AddReferenceColorByCIELAB(self, system: str, name: str, description: str, L: float, a: float, b: float):
		"""		Add a reference color
		Args:
			system (str):
			name (str):
			description (str):
			L (float):
			a (float):
			b (float):
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = [system, name, description, L, a, b]
		ret = None
		def AddReferenceColorByCIELAB_Ret(async_ret):
			nonlocal ret
			ret = async_ret
		pybus.call('ColorConverter.AddReferenceColorByCIELAB', args, AddReferenceColorByCIELAB_Ret)

	def AddReferenceColorByCMYK(self, system: str, name: str, description: str, c: float, m: float, y: float, k: float):
		"""		Add a reference color
		Args:
			system (str):
			name (str):
			description (str):
			c (float):
			m (float):
			y (float):
			k (float):
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = [system, name, description, c, m, y, k]
		ret = None
		def AddReferenceColorByCMYK_Ret(async_ret):
			nonlocal ret
			ret = async_ret
		pybus.call('ColorConverter.AddReferenceColorByCMYK', args, AddReferenceColorByCMYK_Ret)

	def AddReferenceColorByHEX(self, system: str, name: str, description: str, hex: str):
		"""		Add a reference color
		Args:
			system (str):
			name (str):
			description (str):
			hex (str):
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = [system, name, description, hex]
		ret = None
		def AddReferenceColorByHEX_Ret(async_ret):
			nonlocal ret
			ret = async_ret
		pybus.call('ColorConverter.AddReferenceColorByHEX', args, AddReferenceColorByHEX_Ret)

	def AddReferenceColorByXYZ(self, system: str, name: str, description: str, x: float, y: float, z: float):
		"""		Add a reference color
		Args:
			system (str):
			name (str):
			description (str):
			x (float):
			y (float):
			z (float):
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = [system, name, description, x, y, z]
		ret = None
		def AddReferenceColorByXYZ_Ret(async_ret):
			nonlocal ret
			ret = async_ret
		pybus.call('ColorConverter.AddReferenceColorByXYZ', args, AddReferenceColorByXYZ_Ret)

	def FindReferenceColorByRGB(self, r: float, g: float, b: float) -> List[Any]:
		"""		
		Args:
			r (float):
			g (float):
			b (float):
		Returns:
			
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = [r, g, b]
		ret = None
		def FindReferenceColorByRGB_Ret(async_ret):
			nonlocal ret
			ret = async_ret
		pybus.call('ColorConverter.FindReferenceColorByRGB', args, FindReferenceColorByRGB_Ret)
		return ret

	def FindReferenceColorByCIELAB(self, L: float, a: float, b: float) -> List[Any]:
		"""		
		Args:
			L (float):
			a (float):
			b (float):
		Returns:
			
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = [L, a, b]
		ret = None
		def FindReferenceColorByCIELAB_Ret(async_ret):
			nonlocal ret
			ret = async_ret
		pybus.call('ColorConverter.FindReferenceColorByCIELAB', args, FindReferenceColorByCIELAB_Ret)
		return ret

	def FindReferenceColorByCMYK(self, c: float, m: float, y: float, k: float) -> List[Any]:
		"""		
		Args:
			c (float):
			m (float):
			y (float):
			k (float):
		Returns:
			
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = [c, m, y, k]
		ret = None
		def FindReferenceColorByCMYK_Ret(async_ret):
			nonlocal ret
			ret = async_ret
		pybus.call('ColorConverter.FindReferenceColorByCMYK', args, FindReferenceColorByCMYK_Ret)
		return ret

	def FindReferenceColorByHEX(self, hex: str) -> List[Any]:
		"""		
		Args:
			hex (str):
		Returns:
			
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = [hex]
		ret = None
		def FindReferenceColorByHEX_Ret(async_ret):
			nonlocal ret
			ret = async_ret
		pybus.call('ColorConverter.FindReferenceColorByHEX', args, FindReferenceColorByHEX_Ret)
		return ret

	def FindReferenceColorByXYZ(self, x: float, y: float, z: float) -> List[Any]:
		"""		
		Args:
			x (float):
			y (float):
			z (float):
		Returns:
			
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = [x, y, z]
		ret = None
		def FindReferenceColorByXYZ_Ret(async_ret):
			nonlocal ret
			ret = async_ret
		pybus.call('ColorConverter.FindReferenceColorByXYZ', args, FindReferenceColorByXYZ_Ret)
		return ret

	def FindReferenceColor(self, system: str, name: str) -> List[Any]:
		"""		
		Args:
			system (str):
			name (str):
		Returns:
			
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = [system, name]
		ret = None
		def FindReferenceColor_Ret(async_ret):
			nonlocal ret
			ret = async_ret
		pybus.call('ColorConverter.FindReferenceColor', args, FindReferenceColor_Ret)
		return ret

	def RemoveReferenceColorSystem(self, system: str):
		"""		Remove reference color system and all reference colors
		Args:
			system (str):
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = [system]
		ret = None
		def RemoveReferenceColorSystem_Ret(async_ret):
			nonlocal ret
			ret = async_ret
		pybus.call('ColorConverter.RemoveReferenceColorSystem', args, RemoveReferenceColorSystem_Ret)

	def GetReferenceColorSystems(self) -> List[Any]:
		"""		Get all reference color systems
		Returns:
			
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = []
		ret = None
		def GetReferenceColorSystems_Ret(async_ret):
			nonlocal ret
			ret = async_ret
		pybus.call('ColorConverter.GetReferenceColorSystems', args, GetReferenceColorSystems_Ret)
		return ret

	def GetReferenceColors(self, system: str) -> List[Any]:
		"""		Get all reference colors in a color reference system
		Args:
			system (str):
		Returns:
			
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = [system]
		ret = None
		def GetReferenceColors_Ret(async_ret):
			nonlocal ret
			ret = async_ret
		pybus.call('ColorConverter.GetReferenceColors', args, GetReferenceColors_Ret)
		return ret

	def GetIlluminationObserverAngles(self) -> List[Any]:
		"""		Get supported illumination and observer angles
		Returns:
			
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = []
		ret = None
		def GetIlluminationObserverAngles_Ret(async_ret):
			nonlocal ret
			ret = async_ret
		pybus.call('ColorConverter.GetIlluminationObserverAngles', args, GetIlluminationObserverAngles_Ret)
		return ret

	def SaveReferenceColors(self, id: str):
		"""		Save reference colors
		Args:
			id (str):
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = [id]
		ret = None
		def SaveReferenceColors_Ret(async_ret):
			nonlocal ret
			ret = async_ret
		pybus.call('ColorConverter.SaveReferenceColors', args, SaveReferenceColors_Ret)

	def LoadReferenceColors(self, id: str):
		"""		Load reference colors
		Args:
			id (str):
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = [id]
		ret = None
		def LoadReferenceColors_Ret(async_ret):
			nonlocal ret
			ret = async_ret
		pybus.call('ColorConverter.LoadReferenceColors', args, LoadReferenceColors_Ret)




Vector3 = {
--x,y,z
}
function Vector3:new(x, y, z)
    self.__index = self
    self.x = x or 0
    self.y = y or 0
    self.z = z or 0
end
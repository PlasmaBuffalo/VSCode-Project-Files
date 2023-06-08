-- a program to dynamically adjust the height of a ship's pistons to simulate a local terrain map
-- stepDistance: the grid size for terrain altitude checking (in meters)
local stepDistance = 100
-- zeroPoint: the local coordinates for the central piston, placing the ship at the center of the map at all times
-- this value is set by user
local zeroPoint = Vector3(0, 4, 27)

function Update(I)
    local componentCount = I:GetAllSubconstructsCount()
    for i = 0, componentCount, 1 do
        -- get difference in x/z coordinates between the current piston and the zeroPoint
        local pInfo = I:GetSubconstructIdentifier(i)
        I:Log("localPos of ID=" .. pInfo.SubConstructIdentifier .. " is " .. pInfo.LocalPosition.x .. ", " ..
                  pInfo.LocalPosition.y .. ", " .. pInfo.LocalPosition.z)
        -- difference between piston positions: pInfo.LocalPosition - zeroPoint
        local pPosnDiff = pInfo.LocalPosition - zeroPoint
        -- multiply by stepDistance to get the proper point on terrain to checking
        local terrPosnDiff = pPosnDiff * stepDistance
        -- get terrain altitude at this point
        -- set piston height according to terrain altitude
    end -- close for loop
end -- close Update function

--[[
function dump here

I:GetAllSubconstructsCount() -- returns int, number of subconstructs
I:GetSubconstructIdentifier(int index) -- returns int, subconstruct identifier, used to get info in below method
I:GetSubConstructInfo(int SubConstructIdentifier) -- returns BlockInfo{}, contains info about the subconstruct. We'll use this for:
    > .LocalPosition [Vector3]: position in construct (right, up,forwards)
    > .CustomName [string]: the custom name assigned to the block.
]]

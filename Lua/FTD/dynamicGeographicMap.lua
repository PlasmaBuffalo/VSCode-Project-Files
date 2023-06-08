--[[for each piston found:
- get the local position
- get the terrain altitude at that position
- set the piston height to the terrain altitude
]] --[[variables to account for:
 stepDistance: the grid size for terrain altitude checking (in meters)
 pistons will be 1m apart by this hardcoded construction
 terrain checks will be <stepDistance> apart
]] local stepDistance = 100

function Update(I)
    local componentCount = I:Component_GetCount(33)
    for i = 0, componentCount, 1 do
        
    end
end

--[[
function dump here

I:GetAllSubconstructsCount() -- returns int, number of subconstructs
I:GetSubconstructIdentifier(int index) -- returns int, subconstruct identifier, used to get info in below method
I:GetSubConstructInfo(int SubConstructIdentifier) -- returns BlockInfo{}, contains info about the subconstruct. We'll use this for:
    > LocalPosition [Vector3]: position in construct (right, up,forwards)
    > CustomName [string]: the custom name assigned to the block.
]]

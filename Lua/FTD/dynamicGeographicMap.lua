-- a program to dynamically adjust the height of a ship's pistons to simulate a local terrain map
-- stepDistance: the grid size for terrain altitude checking (in meters)
local stepDistance = 100
-- zeroPoint: the local coordinates for the central piston, placing the ship at the center of the map at all times
-- this value is set by user, or else the position differences will be incorrect
local zeroPoint = Vector3.zero
local terrainBounds = {
    lower = -250,
    upper = 250
}

function Update(I)
    local componentCount = I:GetAllSubconstructsCount()
    for i = 0, componentCount, 1 do
        -- only iterating on the pistons, ignore others subconstructs
        if I:GetSubConstructInfo(I:GetSubConstructIdentifier(i)).Valid and I:IsPiston(I:GetSubConstructIdentifier(i)) then
            -- get difference in x/z coordinates between the current piston and the zeroPoint
            local pistonInfo = I:GetSubConstructInfo(I:GetSubConstructIdentifier(i))

            -- if the name of the piston is "zp", set zeroPoint to its local position
            if pistonInfo.CustomName == "zp" then
                zeroPoint = pistonInfo.LocalPosition
                I:Log("zeroPoint is now " .. zeroPoint.x .. ", " .. zeroPoint.y .. ", " .. zeroPoint.z)
            end

            -- difference between piston positions: pInfo.LocalPosition - zeroPoint
            local pistonPosDiff = pistonInfo.LocalPosition - zeroPoint
            I:Log("relative location for ID" .. pistonInfo.SubConstructIdentifier .. " is " ..pistonInfo.LocalPosition.x .. ", " .. pistonInfo.LocalPosition.y .. ", " .. pistonInfo.LocalPosition.z)
            I:Log("pistonPosDiff for ID" .. pistonInfo.SubConstructIdentifier .. " is " .. pistonPosDiff.x .. ", " ..
                      pistonPosDiff.y .. ", " .. pistonPosDiff.z)
            -- multiply by stepDistance to get the proper point on terrain to checking
            local terrainPosDiff = pistonPosDiff * stepDistance
            I:Log("terrainPosDiff for ID" .. pistonInfo.SubConstructIdentifier .. " is " .. terrainPosDiff.x .. ", " ..
                      terrainPosDiff.y .. ", " .. terrainPosDiff.z)
            -- get terrain altitude at this point
            -- set piston height according to terrain altitude
        end -- close if statement
    end -- close for loop
end -- close Update function

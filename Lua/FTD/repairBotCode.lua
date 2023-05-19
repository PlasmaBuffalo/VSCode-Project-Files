-- loop through friendly health values
-- pick the lowest friendly health fraction and go heal that friendly until health fraction is 1.0
-- repeat
-- after an indicated period of time passes, the function will be called again
-- Variables:
-- amount of time to take between function calls (in seconds)
local loopInterval = 10
-- ID of the current friendly construct
local repairID = -1
-- Functions:
-- timer function will return true only if the current time is a multiple of loopInterval
function Timer(I)
    -- get the current time
    local time = Mathf.Floor(I:GetTime() % loopInterval)
    -- whenever time is zero, return true
    if time == 0 then
        return true
    else
        return false
    end -- close if statement
end -- close function

-- HealthScan will return the index of the friendly with the lowest health fraction
function HealthScan(I)

    -- number of friendlies on the field
    local friendlyCount = I:GetFriendlyCount()
    -- variable to store lowest health fraction found in list
    local lowestHealth = 2
    -- index of the friendly with the lowest health fraction
    local lowestHealthIndex = -1

    for index = 0, friendlyCount - 1 do
        local friendlyInfo = I:GetFriendlyInfo(index)
        local healthFraction = friendlyInfo.HealthFraction
        if healthFraction < lowestHealth then
            lowestHealth = healthFraction
            lowestHealthIndex = index
        end -- close if statement
        I:Log(string.format("Friendly %d - Health Fraction: %.2f", index, healthFraction))
    end -- close for loop
    return lowestHealthIndex
end -- close function

-- TrackFriendly will move the repairbot in range of the friendly with the lowest health fraction
function TrackFriendly(I)
    -- first, we get the position of the friendly to repair (in world coordinates)
    local friendlyInfo = I:GetFriendlyInfo(repairID)
    local friendlyPos = friendlyInfo.ReferencePosition
    -- then, we get the position of the repair bot (in world coordinates)
    local botPos = I:GetConstructPosition()
    -- then, we get the vector from the bot to the friendly
    local vectorToFriendly = friendlyPos - botPos
    -- TODO - make the bot move towards the friendly
    -- will try to do this by rotating the bot to face the friendly and issuing a forward thrust command
end
-- Update will run the program
function Update(I)
    if Timer(I) then
        repairID = HealthScan(I)
        I:LogToHud("Repair Target ID: " .. repairID .. " named " .. I:GetFriendlyInfo(repairID).BlueprintName)
    else -- if Timer(I) is false
        TrackFriendly(I)
    end
    -- close conditional
end
-- close main function

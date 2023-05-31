-- loop through friendly health values
-- pick the lowest friendly health fraction and go heal that friendly until health fraction is 1.0
-- repeat
-- after an indicated period of time passes, the function will be called again
-- Variables:
-- amount of time to take between function calls (in seconds)
    local loopInterval = 10
    -- ID of the current friendly construct
    local repairID = -1
    -- yaw tolerance for the repair bot (in degrees)
    local yawTolerance = 5

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

    -- TargetAhead will return true if the friendly to repair is within the yawTolerance of the repair bot's forward vector
    function TargetAhead(I)
        -- get positions of bot and friendly to repair (world coordinates)
        local botPos = I:GetConstructPosition()
        local friendlyPos = I:GetFriendlyInfo(repairID).ReferencePosition
        -- set y component of positions to 0; this is for comparison purposes
        botPos.y = 0
        friendlyPos.y = 0

        -- get the vector from the bot to the friendly
        local vectorToFriendly = friendlyPos - botPos

        -- get signed angle between the two vectors. Sign matters since we choose whether to turn left or right
        local angleDelta = Vector3.SignedAngle(I:GetConstructForwardVector(), vectorToFriendly, Vector3.up)

        -- if the difference in angle is greater than tolerance level, return false
        if Mathf.Abs(angleDelta) - yawTolerance > 0 then
            return false
        else -- if the difference in angle is less than tolerance level, return true
            return true
        end
    end

    -- TrackFriendly will move the repairbot in range of the friendly with the lowest health fraction
    function TrackFriendly(I)
        -- get positions of bot and friendly to repair (world coordinates)
        local botPos = I:GetConstructPosition()
        local friendlyPos = I:GetFriendlyInfo(repairID).ReferencePosition
        -- set y component of positions to 0; this is for comparison purposes
        botPos.y = 0
        friendlyPos.y = 0

        -- get the vector from the bot to the friendly
        local vectorToFriendly = friendlyPos - botPos

        -- get signed angle between the two vectors. Sign matters since we choose whether to turn left or right
        local angleDelta = Vector3.SignedAngle(I:GetConstructForwardVector(), vectorToFriendly, Vector3.up)
        -- little debug spinblock to show where we think the friendly is
        I:SetSpinBlockRotationAngle(2, angleDelta)
        I:Log("Angle difference 1: " .. angleDelta)

        -- if the friendly is ahead of the bot, move forward
        if TargetAhead(I) then
            --get forward amount, increasing thrust as distance increases
            local forwardAmount = (vectorToFriendly.magnitude - 100) * 0.01
            I:SetPropulsionRequest(0, forwardAmount)
        else -- we need to adjust yaw
            --stop moving forward
            I:SetPropulsionRequest(0, 0)
            --get relevant yaw values
            local yawVelocity = I:GetLocalAngularVelocity().y
            local yawRequest = (angleDelta / 180) - Mathf.Clamp01(yawVelocity / 10)
            -- make propulsion request
            I:SetPropulsionRequest(5, yawRequest)
        end
    end
    -- Update will run the program
    function Update(I)
        I:ClearLogs()
        if Timer(I) then
            repairID = HealthScan(I)
            I:LogToHud("Repair Target ID: " .. repairID .. " named " .. I:GetFriendlyInfo(repairID).BlueprintName)
        else -- if Timer(I) is false
            TrackFriendly(I)
        end
        -- close conditional
    end
    -- close main function

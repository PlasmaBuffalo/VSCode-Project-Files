function Update(I)
    local speedFactor = 4
    local maxAngle = 45

    -- Get the current time in seconds
    local time = I:GetTime()

    -- Calculate the angle to use based on whether the time is even or odd
    local angle = math.floor(time*speedFactor) % 2 == 0 and maxAngle or -maxAngle

    -- Set the angle of the spin block with the given SubConstructIdentifier
    I:SetSpinBlockRotationAngle(32, angle)

    -- Print a log statement to show the current time and angle being used
    I:Log(string.format("Time: %d, Angle: %d", time, angle))
end

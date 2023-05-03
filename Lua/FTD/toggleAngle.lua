function Update(I)
    -- Get the current time in seconds
    local time = I:GetTime()

    -- Calculate the angle to use based on whether the time is even or odd
    local angle = math.floor(time) % 2 == 0 and 45 or -45

    -- Set the angle of the spin block with the given SubConstructIdentifier
    I:SetSpinBlockRotationAngle(SubConstructIdentifier, angle)

    -- Print a log statement to show the current time and angle being used
    I:Log(string.format("Time: %d, Angle: %d", time, angle))
end

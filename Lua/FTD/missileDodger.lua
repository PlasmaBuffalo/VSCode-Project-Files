function Update(I)
    -- Check if there are any warnings
    local numberOfWarnings = I:GetNumberOfWarnings()

    -- If there are warnings, set propulsion request for 3 seconds
    if numberOfWarnings > 0 then
        -- Display a message to the user on the HUD
        I:LogToHud("Warning detected!")

        -- Set propulsion request to -1 (downward direction)
        I:SetPropulsionRequest(7, -1)

        -- Wait for 3 seconds
        local startTime = I:GetTime()
        while I:GetTime() - startTime < 3 do
            I:Yield()
        end

        -- Reset propulsion request to 0 (no thrust)
        I:SetPropulsionRequest(7, 0)
    end
end

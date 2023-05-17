-- A program to constantly log the health fraction of all friendly vehicles
function Update(I)

    local friendlyCount = I:GetFriendlyCount()

    for index = 0, friendlyCount - 1 do
        local friendlyInfo = I:GetFriendlyInfo(index)
        local healthFraction = friendlyInfo:Get("HealthFraction")
        I:Log(string.format("Friendly %d - Health Fraction: %.2f", index, healthFraction))
    end -- close for loop
end -- close Update function

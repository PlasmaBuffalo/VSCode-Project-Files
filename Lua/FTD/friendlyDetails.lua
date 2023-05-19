-- A program to constantly log the health fraction of all friendly vehicles
function HealthScan(I)

    -- number of friendlies on the field
    local friendlyCount = I:GetFriendlyCount()
    -- variable to store lowest health fraction found in list
    local lowestHealth = 2
    -- index of the friendly with the lowest health fraction
    local lowestHealthIndex = -1

    for index = 0, friendlyCount - 1 do
        local friendlyInfo = I:GetFriendlyInfo(index)
        local healthFraction = friendlyInfo:Get("HealthFraction")
        if healthFraction < lowestHealth then
            lowestHealth = healthFraction
            lowestHealthIndex = index
        end -- close if statement
        I:Log(string.format("Friendly %d - Health Fraction: %.2f", index, healthFraction))
    end -- close for loop
    return lowestHealthIndex
end -- close function

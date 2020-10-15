struct Enemy {
    var health: Int
    var attackStrength: Int
    
    init(health: Int, attackStrength: Int) {
        self.health = health
        self.attackStrength = attackStrength
    }
    
    mutating func takeDamage(amount: Int) {
        health = health - amount
    }
    
    func move() {
        print("Walks forwards.")
        
    }
    
    func attack() {
        print("Land a hit, does \(attackStrength) damage.")
        
    }
}

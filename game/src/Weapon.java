public class Weapon {
    private String name;
    private int damage;
    private int hp;

    public Weapon(String name, int damage, int hp) {
        this.name = name;
        this.damage = damage;
        this.hp = hp;
    }

    public int getHp() {
        return this.hp;
    }

    public int getDamage() {
        return damage;
    }

    public String getName() {
        return this.name;
    }
}

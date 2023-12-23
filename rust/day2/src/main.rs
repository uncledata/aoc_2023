use std::fs::read_to_string;
use std::collections::HashMap;

fn main() {
    let mut color_map = HashMap::new();
    color_map.insert("red", 12);
    color_map.insert("green", 13);
    color_map.insert("blue", 14);
    let mut valids = 0i32;
    for line in read_to_string("./input.txt")
    .expect("failed to read file")
    .lines()
    {
        let (game_id, valid) = parse_line(line, color_map.clone());
        
        if valid {
            valids = valids.checked_add(game_id).expect("overflow");
        }
    }
    println!("valids: {}", valids);
}

fn parse_line(line:&str, color_map:HashMap<&str, i32>) -> (i32, bool) {
    let game = line.split(":").collect::<Vec<&str>>();
    let game_id = game[0].split(" ").collect::<Vec<&str>>()[1].parse::<i32>().expect("failed to parse");
    let games = game[1].split(";").collect::<Vec<&str>>();
    
    for game in games{
        let to_check:Vec<&str> = game.trim().split(",").collect();
        for one_check in to_check
        {
            let check = one_check.trim().split(" ").collect::<Vec<&str>>();
            let color = check[1];
            let value = check[0].parse::<i32>().expect("failed to parse");
            if value>color_map[color] {
                return (game_id, false);
            }
        }
    }
    (game_id, true)

}

use std::io;
use std::cmp::Ordering;
use rand::Rng;

//Rust needs this. Entry point.
fn main() {
    //! in rust is a macro.
    println!("Guess the number!");

    //i32 - 32 bit number.
    //.. - Makes an i32 range.
    let secret_number = rand::thread_rng().gen_range(1..101);
    
    loop {
        println!("Please input your guess...");
    
        //mut - Variable can be modified. By default they are immutable.
        //::new(); - This is a static method.
        let mut guess = String::new();
    
        //io::stdin() - Just calling the module we imported above.
        //.read_line() - Reads a line from the terminal.
        //.expect() - Similar to try and expect but actually neat thanks rust.
        //& - Calls a reference. Means the program won't copy said variable but will instead point to it.
        io::stdin().read_line(&mut guess).expect("Failed to read input.");
    
        //Trim() / Parse() - Make sure the line doesn't have extra data accidentally added.
        //Woah, some cool error catching here.
        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => {println!("Invalid number.");continue;},
        };
    
        //Similar to .format in python.
        println!("You guessed: {}", guess);
    
        //Rust calls these arms but they are just like branches.
        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            //Uses {} to run multiple lines. Same as other languages.
            Ordering::Equal => {println!("You got it!"); break;},
        }
    }
}
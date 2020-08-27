// The objective of this challenge is to apply the skills you learned in the Dicee tutorial and get you making an app with functionality all by yourself. There’s no new concepts here. But you’re flyin’ solo this time! Most of the programming skills are gained in the challenges rather than the tutorials. It’s when you’re using your new-found programming skills to bend the app to your will that you’re truly levelling up as a developer.
// What you will create
// We’re going to make a Magic 8 Ball app. You can ask the app to make all your hard decisions! With this app in your pocket, you’ll always have an answer to life’s many conundrums!

import UIKit

class ViewController: UIViewController {
    
    let ballArray = [#imageLiteral(resourceName: "ball1.png"),#imageLiteral(resourceName: "ball2.png"),#imageLiteral(resourceName: "ball3.png"),#imageLiteral(resourceName: "ball4.png"),#imageLiteral(resourceName: "ball5.png")]
    
    @IBOutlet weak var imageView: UIImageView!
    
    @IBAction func askButtonPressed(_sender:UIButton){
    
    }
}



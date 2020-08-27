// You will program a trivia quiz app. If you have another field of expertise such as law or medicine, you’ll be glad to know that multiple choice question apps are one of the most popular types of educational apps on the App Store! 

import Foundation

struct Question {
    let text: String
    let answerChoices: [String]
    let rightAnswer: String
    
    
    init(q: String, a: [String], c: String) {
        text = q
        answerChoices = a
        rightAnswer = c
    }
}

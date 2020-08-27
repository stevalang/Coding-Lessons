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

import csv
import random
import os

def read_vocabulary_from_csv(file_path):
    wordlist = []
    if not os.path.exists(file_path):
        print(f"Tệp không tồn tại: {file_path}")
        exit(1)

    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                wordlist.append({
                    'expression': row['expression'],
                    'reading': row['reading'],
                    'meaning': row['meaning'],
                    'tags': row['tags']
                })
    except Exception as e:
        print(f"Lỗi khi đọc tệp CSV: {e}")
        exit(1)

    return wordlist

def generate_question(wordlist):
    word = random.choice(wordlist)
    correct_answer = word['meaning']
    incorrect_answers = ["Không biết", "Sai lầm", "Không có nghĩa"]
    answers = [correct_answer] + incorrect_answers
    random.shuffle(answers)

    return f"Ý nghĩa của từ '{word['expression']}' (đọc là '{word['reading']}') là gì?", answers, correct_answer

def run_quiz(wordlist, total_questions=5):
    score = 0
    for i in range(total_questions):
        print(f"\nCâu hỏi {i+1}:")
        question, answers, correct_answer = generate_question(wordlist)
        print(question)
        for idx, ans in enumerate(answers):
            print(f"{idx + 1}. {ans}")

        try:
            user_answer = int(input("Chọn đáp án (1/2/3): "))
            if answers[user_answer - 1] == correct_answer:
                print("Đúng rồi!")
                score += 1
            else:
                print(f"Sai rồi! Đáp án đúng là: {correct_answer}")
        except (ValueError, IndexError):
            print("Lựa chọn không hợp lệ. Vui lòng chọn 1, 2 hoặc 3.")

    print(f"\nBài thi kết thúc! Bạn được {score}/{total_questions} câu đúng.")

if __name__ == "__main__":
    file_path = r"assets/n3.csv"  # Đảm bảo bạn có file 'n3.csv' trong thư mục 'assets'
    wordlist = read_vocabulary_from_csv(file_path)
    print("Chào mừng bạn đến với bài thi trắc nghiệm tiếng Nhật!")
    run_quiz(wordlist)

import tkinter as tk
from tkinter import messagebox
import random
import datetime
import calendar
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import os
import pandas as pd
import platform
import subprocess
import koreanize_matplotlib

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


study_records_df = pd.DataFrame(columns=['date', 'subject', 'hours'])
main_root_window = None
last_chosen_subject = None
all_available_subjects = []



DATA_FILE = "study_data.csv"
STUDY_MATERIALS_DIR = "study_materials"

def save_study_data():
    
    try:
        study_records_df.to_csv(DATA_FILE, index=False, encoding='utf-8-sig')
        print("학습 데이터가 성공적으로 저장되었습니다.")
    except Exception as e:
        messagebox.showerror("저장 오류", f"학습 데이터 저장 중 오류 발생: {e}")

def load_study_data():
    
    global study_records_df
    if os.path.exists(DATA_FILE):
        try:
            study_records_df = pd.read_csv(DATA_FILE, encoding='utf-8-sig')
            study_records_df['date'] = pd.to_datetime(study_records_df['date'], errors='coerce')
            study_records_df.dropna(subset=['date'], inplace=True)
            print("학습 데이터가 성공적으로 불러와졌습니다.")
        except pd.errors.EmptyDataError:
            messagebox.showwarning("데이터 로드 오류", "학습 데이터 파일이 비어있습니다.\n새로운 파일을 생성합니다.")
            study_records_df = pd.DataFrame(columns=['date', 'subject', 'hours'])
        except Exception as e:
            messagebox.showwarning("데이터 로드 오류", f"학습 데이터 파일을 불러오는 중 오류 발생: {e}\n새로운 파일을 생성합니다.")
            study_records_df = pd.DataFrame(columns=['date', 'subject', 'hours'])
    else:
        print("기존 학습 데이터 파일이 없습니다. 새 파일을 생성합니다.")
        study_records_df = pd.DataFrame(columns=['date', 'subject', 'hours'])



def load_subjects_from_folder():
    materials_path = os.path.join(os.path.dirname(__file__), STUDY_MATERIALS_DIR)
    
    if not os.path.exists(materials_path):
        messagebox.showwarning("폴더 없음",
                               f"'{STUDY_MATERIALS_DIR}' 폴더가 없습니다.\n"
                               "스크립트와 같은 위치에 이 폴더를 생성하고\n"
                               "그 안에 공부할 과목 폴더들을 넣어주세요.")
        return []

    subjects = [d for d in os.listdir(materials_path)
                if os.path.isdir(os.path.join(materials_path, d))]
    
    if not subjects:
        messagebox.showwarning("과목 없음",
                               f"'{STUDY_MATERIALS_DIR}' 폴더 안에 과목 폴더가 없습니다.\n"
                               "공부할 과목 이름으로 폴더를 만들어주세요 (예: 수학, 영어).")
    
    return subjects


def open_folder(path):
    system = platform.system()
    if system == "Windows":
        os.startfile(path)
    elif system == "Darwin":
        subprocess.run(["open", path])
    elif system == "Linux":
        subprocess.run(["xdg-open", path])
    else:
        messagebox.showwarning("운영체제 인식 오류", f"지원하지 않는 운영체제입니다: {system}")



def record_study_time_and_update_ui(subject, hours):
    
    global study_records_df
    
    today_date_obj = datetime.date.today()
    
    
    existing_record_mask = (study_records_df['date'] == pd.Timestamp(today_date_obj)) & \
                           (study_records_df['subject'] == subject)

    if not study_records_df[existing_record_mask].empty:
        
        study_records_df.loc[existing_record_mask, 'hours'] += hours
    else:
        
        new_row = pd.DataFrame([{'date': pd.Timestamp(today_date_obj), 'subject': subject, 'hours': hours}])
        study_records_df = pd.concat([study_records_df, new_row], ignore_index=True)
    
    
    save_study_data()
    
    
    study_time_entry.delete(0, tk.END)
    study_time_entry.config(state=tk.DISABLED)
    record_study_button.config(state=tk.DISABLED)
    
    drawn_subject_label.config(text="과목을 선택하거나 뽑아주세요!", fg="darkred")
    global last_chosen_subject
    last_chosen_subject = None


def show_required_subject_time_input(subject):
    
    time_input_window = tk.Toplevel(main_root_window)
    time_input_window.title(f"'{subject}' 학습 시간 기록")
    time_input_window.geometry("350x200")
    time_input_window.grab_set()

    tk.Label(time_input_window, text=f"'{subject}'을(를) 몇 시간 공부했나요?",
             font=("Arial", 14, "bold"), pady=10).pack()
    
    time_entry = tk.Entry(time_input_window, width=10, font=("Arial", 14), justify='center')
    time_entry.pack(pady=5)
    time_entry.focus_set()

    def confirm_time():
        try:
            study_hours = float(time_entry.get())
            if study_hours <= 0:
                raise ValueError
            
            record_study_time_and_update_ui(subject, study_hours)
            messagebox.showinfo("기록 완료", f"'{subject}'을(를) {study_hours}시간 공부했습니다.")
            time_input_window.destroy()
        except ValueError:
            messagebox.showerror("입력 오류", "유효한 공부 시간을 숫자로 입력해주세요 (예: 2.5)")

    tk.Button(time_input_window, text="기록하기", command=confirm_time,
              font=("Arial", 12, "bold"), bg="#4CAF50", fg="white").pack(pady=10)
    
    
    tk.Button(time_input_window, text="닫기 (기록하지 않음)", command=time_input_window.destroy,
              font=("Arial", 10), bg="#FF6347", fg="white").pack(pady=5)



def confirm_required_subject():
    global last_chosen_subject
    
    
    input_window = tk.Toplevel(main_root_window)
    input_window.title("오늘의 필수 과목 입력")
    input_window.geometry("400x200")
    input_window.grab_set()

    tk.Label(input_window, text="오늘의 필수 과목 이름을 정확히 입력해주세요:",
             font=("Arial", 12, "bold"), pady=10).pack()
    
    subject_entry = tk.Entry(input_window, width=30, font=("Arial", 12), justify='center')
    subject_entry.pack(pady=5)
    subject_entry.focus_set()

    def process_subject():
        entered_subject = subject_entry.get().strip()
        if not entered_subject:
            messagebox.showwarning("입력 오류", "과목 이름을 입력해주세요!")
            return
        
        
        subject_folder_path = os.path.join(os.path.dirname(__file__), STUDY_MATERIALS_DIR, entered_subject)
        if not os.path.exists(subject_folder_path) or not os.path.isdir(subject_folder_path):
            messagebox.showerror("과목 없음", f"'{entered_subject}' 과목 폴더를 찾을 수 없습니다.\n'study_materials' 폴더에 해당 과목 폴더가 있는지 확인해주세요.")
            return

        
        open_folder(subject_folder_path)

        
        response = messagebox.askyesno("과제 완료 확인", f"오늘 '{entered_subject}' 과제를 끝내셨습니까?")
        
        if response:
            drawn_subject_label.config(text=f"오늘의 필수 과목: {entered_subject}", fg="purple")
            last_chosen_subject = entered_subject
            show_required_subject_time_input(entered_subject)
        else:
            drawn_subject_label.config(text="과목을 선택하거나 뽑아주세요!", fg="darkred")
            last_chosen_subject = None
            messagebox.showinfo("안내", f"'{entered_subject}' 과목 기록이 취소되었습니다.")
        
        input_window.destroy()

    tk.Button(input_window, text="확인", command=process_subject,
              font=("Arial", 12, "bold"), bg="#1E90FF", fg="white").pack(pady=10)
    
    
    tk.Button(input_window, text="닫기 (기록하지 않음)", command=input_window.destroy,
              font=("Arial", 10), bg="#FF6347", fg="white").pack(pady=5)



def draw_random_subject():
    global last_chosen_subject
    
    
    
    drawable_subjects = [s for s in all_available_subjects if s != last_chosen_subject]

    if not drawable_subjects:
        if all_available_subjects:
            messagebox.showwarning("오류", "랜덤으로 뽑을 수 있는 과목이 없습니다.\n"
                                          "모든 과목이 필수 과목으로 처리되었거나, 과목 폴더가 비어 있습니다.")
        else:
            messagebox.showwarning("오류", "공부할 과목 폴더가 없습니다. 'study_materials' 폴더에 과목 폴더를 만들어주세요!")
        return
    
    drawn_subject = random.choice(drawable_subjects)
    
    drawn_subject_label.config(text=f"오늘의 랜덤 과목: {drawn_subject}", fg="blue")
    
    last_chosen_subject = drawn_subject
    
    
    study_time_entry.config(state=tk.NORMAL)
    record_study_button.config(state=tk.NORMAL)

    subject_folder_path = os.path.join(os.path.dirname(__file__), STUDY_MATERIALS_DIR, drawn_subject)
    if os.path.exists(subject_folder_path):
        open_folder(subject_folder_path)
    else:
        messagebox.showwarning("폴더 없음", f"'{drawn_subject}' 과목 폴더를 찾을 수 없습니다.\n경로를 확인해주세요.")


def record_from_main_ui():
    
    global last_chosen_subject
    if not last_chosen_subject:
        messagebox.showwarning("기록 오류", "먼저 과목을 선택하거나 뽑아주세요!")
        return

    try:
        study_hours = float(study_time_entry.get())
        if study_hours <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("입력 오류", "유효한 공부 시간을 숫자로 입력해주세요 (예: 2.5시간)")
        return
    
    
    record_study_time_and_update_ui(last_chosen_subject, study_hours)
    messagebox.showinfo("기록 완료", f"'{last_chosen_subject}'을(를) {study_hours}시간 공부했습니다.")



def show_calendar():
    calendar_window = tk.Toplevel(main_root_window)
    calendar_window.title("월별 학습 캘린더")
    calendar_window.geometry("700x500")

    current_year = datetime.date.today().year
    current_month = datetime.date.today().month

    tk.Label(calendar_window, text=f"{current_year}년 {current_month}월", font=("Arial", 18, "bold")).pack(pady=10)

    days_of_week = ["월", "화", "수", "목", "금", "토", "일"]
    day_frame = tk.Frame(calendar_window)
    day_frame.pack()
    for i, day in enumerate(days_of_week):
        tk.Label(day_frame, text=day, width=8, font=("Arial", 10, "bold"), fg="gray").grid(row=0, column=i, padx=2, pady=2)

    date_grid_frame = tk.Frame(calendar_window)
    date_grid_frame.pack()

    cal = calendar.Calendar()
    month_days = cal.monthdayscalendar(current_year, current_month)

    
    monthly_records = study_records_df[
        (study_records_df['date'].dt.year == current_year) &
        (study_records_df['date'].dt.month == current_month)
    ]
    
    for week_idx, week in enumerate(month_days):
        for day_idx, day in enumerate(week):
            if day != 0:
                current_date = datetime.date(current_year, current_month, day)
                daily_records = monthly_records[monthly_records['date'].dt.date == current_date]
                
                if not daily_records.empty:
                    total_hours_on_day = daily_records['hours'].sum()
                    bg_color = "lightgreen"
                    fg_color = "blue"
                    
                    info_lines = [f"{current_date.strftime('%Y-%m-%d')}: 총 {total_hours_on_day:.1f}시간"]
                    for subject in daily_records['subject'].unique():
                        subject_hours = daily_records[daily_records['subject'] == subject]['hours'].sum()
                        info_lines.append(f"  - {subject}: {subject_hours:.1f}시간")
                    tooltip_text = "\n".join(info_lines)

                else:
                    bg_color = "white"
                    fg_color = "black"
                    tooltip_text = f"{current_date.strftime('%Y-%m-%d')}: 기록 없음"

                date_label = tk.Label(date_grid_frame, text=str(day), width=8, height=1, font=("Arial", 10, "bold"),
                                       bg=bg_color, fg=fg_color, relief="groove")
                date_label.grid(row=week_idx + 1, column=day_idx, padx=2, pady=2, sticky="nsew")
                
                date_label.bind("<Button-1>", lambda e, info=tooltip_text: messagebox.showinfo("학습 상세", info))

            else:
                tk.Label(date_grid_frame, text="", width=8, height=1, bg="lightgray", relief="flat").grid(row=week_idx + 1, column=day_idx, padx=2, pady=2, sticky="nsew")
            
    tk.Button(calendar_window, text="닫기", command=calendar_window.destroy, font=("Arial", 12)).pack(pady=10)



def show_graph():
    
    if study_records_df.empty:
        messagebox.showwarning("데이터 없음", "아직 기록된 공부 시간이 없습니다.")
        return

    subject_total_hours = study_records_df.groupby('subject')['hours'].sum().reset_index()
    
    if subject_total_hours.empty:
        messagebox.showwarning("데이터 없음", "아직 기록된 공부 시간이 없습니다.")
        return

    subjects = subject_total_hours['subject'].tolist()
    hours = subject_total_hours['hours'].tolist()

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(subjects, hours, color='skyblue')
    ax.set_xlabel("과목", fontsize=12)
    ax.set_ylabel("총 공부 시간 (시간)", fontsize=12)
    ax.set_title("과목별 순공 시간", fontsize=16)
    ax.tick_params(axis='x', rotation=45, labelsize=10)
    plt.tight_layout()

    graph_window = tk.Toplevel(main_root_window)
    graph_window.title("과목별 순공 시간 그래프")
    graph_window.geometry("800x700")

    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, graph_window)
    toolbar.update()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    tk.Button(graph_window, text="닫기", command=lambda: [plt.close(fig), graph_window.destroy()], font=("Arial", 12)).pack(pady=10)



def create_main_뽑기_ui():
    
    
    for widget in main_root_window.winfo_children():
        widget.destroy()

    main_frame = tk.Frame(main_root_window, bg="lightcyan", padx=20, pady=20)
    main_frame.pack(fill=tk.BOTH, expand=True)

    
    tk.Label(main_frame, text="오늘의 공부",
             font=("Arial", 28, "bold"), bg="lightcyan", fg="darkgreen").pack(pady=(30, 10))

    global drawn_subject_label
    drawn_subject_label = tk.Label(main_frame, text="과목을 선택하거나 뽑아주세요!",
                                   font=("Arial", 26, "bold"), bg="lightcyan", fg="darkred",
                                   wraplength=700)
    drawn_subject_label.pack(pady=20)


    button_frame = tk.Frame(main_frame, bg="lightcyan")
    button_frame.pack(pady=25)

    
    confirm_req_button = tk.Button(button_frame, text="✅ 오늘의 필수 과목 확인", command=confirm_required_subject,
                                   font=("Arial", 16, "bold"), bg="#FF6347", fg="white",
                                   activebackground="#E55337", padx=15, pady=8)
    confirm_req_button.pack(side=tk.LEFT, padx=15)


    draw_random_button = tk.Button(button_frame, text="🎲 랜덤 과목 뽑기!", command=draw_random_subject,
                            font=("Arial", 16, "bold"), bg="#FFD700", fg="black",
                            activebackground="#FFC700", padx=15, pady=8)
    draw_random_button.pack(side=tk.LEFT, padx=15)

    
    study_input_frame = tk.Frame(main_frame, bg="lightcyan")
    study_input_frame.pack(pady=(30, 15))

    tk.Label(study_input_frame, text="선택/뽑힌 과목을 몇 시간 공부했나요?", font=("Arial", 16), bg="lightcyan").pack(side=tk.LEFT, padx=10)
    
    global study_time_entry
    study_time_entry = tk.Entry(study_input_frame, width=10, font=("Arial", 16), justify='center')
    study_time_entry.pack(side=tk.LEFT, padx=10)
    study_time_entry.config(state=tk.DISABLED)

    global record_study_button
    record_study_button = tk.Button(study_input_frame, text="기록하기", command=record_from_main_ui,
                                    font=("Arial", 16), bg="#ADD8E6", activebackground="#9ACCE0", padx=15, pady=8)
    record_study_button.pack(side=tk.LEFT, padx=10)
    record_study_button.config(state=tk.DISABLED)


    
    control_buttons_frame = tk.Frame(main_frame, bg="lightcyan")
    control_buttons_frame.pack(pady=30)

    tk.Button(control_buttons_frame, text="📅 달력 보기", command=show_calendar,
              font=("Arial", 14), bg="#E0E0E0", activebackground="#D0D0D0", padx=20, pady=10).pack(side=tk.LEFT, padx=20)
    
    tk.Button(control_buttons_frame, text="📊 그래프 보기", command=show_graph,
              font=("Arial", 14), bg="#E0E0E0", activebackground="#D0D0D0", padx=20, pady=10).pack(side=tk.LEFT, padx=20)


def main():
    
    global main_root_window
    main_root_window = tk.Tk()
    main_root_window.title("공부 뽑기 플래너 v3.1")
    main_root_window.geometry("800x700")
    main_root_window.resizable(False, False)

    
    load_study_data()
    
    
    global all_available_subjects
    all_available_subjects = load_subjects_from_folder()

    main_root_window.protocol("WM_DELETE_WINDOW", lambda: [save_study_data(), main_root_window.destroy()])

    
    
    try:
        plt.figure()
        plt.close()
    except Exception:
        messagebox.showwarning("Matplotlib 라이브러리 필요",
                               "그래프 기능을 사용하려면 'matplotlib' 라이브러리가 필요합니다.\n"
                               "명령 프롬프트(cmd)나 터미널에서 'pip install matplotlib'를 실행하여 설치해주세요.")

    try:
        pd.DataFrame()
    except NameError:
        messagebox.showwarning("Pandas 라이브러리 필요",
                               "데이터 관리 기능을 사용하려면 'pandas' 라이브러리가 필요합니다.\n"
                               "명령 프롬프트(cmd)나 터미널에서 'pip install pandas'를 실행하여 설치해주세요.")

    create_main_뽑기_ui()
    main_root_window.mainloop()

if __name__ == "__main__":
    main()
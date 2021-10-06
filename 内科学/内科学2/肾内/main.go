package main

import (
	"fmt"
	"log"
	"os"
	"regexp"
	"strings"
)

var alphaBet = "ABCDEFGH"
var allAns = "BCAEABDACDDECDABCEDCDCEABCBEBCBDACDCBBAEEEABCCCCCCACDCABCEDDCEADCCABACACEAECBADDBAEDCBECCCDEADCCCEEBACED"

func main() {
	//getChoose()
	//removeChoose()
	processA1()
	//processX()
}

// 处理a1a2题
func processA1() {
	b, _ := os.ReadFile("a1.txt")
	lines := strings.Split(strings.TrimSpace(string(b)), "\n")
	f, _ := os.Create("anki_choose.txt")
	defer f.Close()

	for i, v := range lines {
		v = strings.TrimSpace(v)

		tnc := strings.Split(v, "\t")
		if len(tnc) != 2 {
			log.Fatalf("%s\n    该行没有制表符分隔\n", v)
		}

		title := tnc[0]
		choices := strings.Split(tnc[1], "||")
		if len(choices) != 5 {
			log.Fatalf("%s\n    该行选项不足五个\n", v)
		}

		ans := allAns[i]
		ansIndex := strings.IndexByte(alphaBet, ans)
		if ansIndex == -1 {
			log.Fatalf("%s\n    该行答案不匹配\n", v)
		}
		title = strings.TrimSpace(title) + "{{c1::}}"

		fmt.Fprintf(f, "%d\t%s\t%s\t%d\n", i+1, title, tnc[1], ansIndex+1)
	}
}

// 处理x型题
func processX() {
	b, _ := os.ReadFile("x.txt")
	lines := strings.Split(strings.TrimSpace(string(b)), "\r\n")
	f, _ := os.Create("anki_x.txt")

	for i, v := range lines {
		v = strings.TrimSpace(v)

		tnc := strings.Split(v, "\t")
		if len(tnc) != 2 {
			log.Fatalf("%s\n    该行没有制表符分隔\n", v)
		}

		title := tnc[0]
		choices := strings.Split(tnc[1], "||")
		if len(choices) < 5 {
			log.Fatalf("%s\n    该行选项不足五个\n", v)
		}

		ans := regexp.MustCompile(`[A-H]{2,}$`).FindString(title)
		if ans == "" {
			log.Fatalf("%s\n    该行不是多选题\n", v)
		}

		ansArr := []string{}
		for i := 0; i < len(ans); i++ {
			ansIndex := strings.IndexByte(alphaBet, ans[i])
			if ansIndex == -1 {
				log.Fatalf("%s\n    该行答案不匹配\n", v)
			}
			ansArr = append(ansArr, fmt.Sprintf("%d", ansIndex+1))
		}

		ansStr := strings.Join(ansArr, "||")
		title = strings.TrimSuffix(title, ans)
		title = strings.TrimSpace(title) + "{{c1::}}"

		fmt.Fprintf(f, "%d\t%s\t%s\t%s\n", i+1, title, tnc[1], ansStr)
	}
}

// 从正本习题中，根据提取的选择题的排除获取全部非选择题
func removeChoose() {
	b, _ := os.ReadFile("选择.txt")
	chooseLines := strings.Split(string(b), "\n")

	b1, _ := os.ReadFile("肾内.txt")
	allLines := strings.Split(string(b1), "\n")

	f, _ := os.Create("非选择.txt")
	defer f.Close()

	ok := false
	for _, line := range allLines {
		line = strings.TrimSpace(line)

		ok = true
		for _, v := range chooseLines {
			v = strings.TrimSpace(v)

			if line == v {
				//chooseLines = chooseLines[i:]
				ok = false
				break
			}
		}

		if !ok {
			continue
		}

		fmt.Fprintln(f, line)
	}
}

// 从整本习题中获取全部选择题
func getChoose() {
	b, _ := os.ReadFile("肾内.txt")
	lines := strings.Split(string(b), "\r\n")
	f, _ := os.Create("选择.txt")
	defer f.Close()

	ok := false
	for _, line := range lines {
		if strings.Contains(line, "选择题") {
			ok = true
		} else if regexp.MustCompile(`^[一二三四五六七]`).MatchString(line) {
			ok = false
		}

		if !ok {
			continue
		}

		fmt.Fprintln(f, line)
	}
}

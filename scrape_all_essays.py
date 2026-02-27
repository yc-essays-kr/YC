import os
import time
import re
from playwright.sync_api import sync_playwright

# 중복 제거된 에세이 목록
essays = [
    {"title": "How to Do Great Work", "url": "greatwork.html"},
    {"title": "Having Kids", "url": "kids.html"},
    {"title": "How to Lose Time and Money", "url": "selfindulgence.html"},
    {"title": "The Shape of the Essay Field", "url": "field.html"},
    {"title": "Good Writing", "url": "goodwriting.html"},
    {"title": "What to Do", "url": "do.html"},
    {"title": "The Origins of Wokeness", "url": "woke.html"},
    {"title": "Writes and Write-Nots", "url": "writes.html"},
    {"title": "When To Do What You Love", "url": "when.html"},
    {"title": "Founder Mode", "url": "foundermode.html"},
    {"title": "The Right Kind of Stubborn", "url": "persistence.html"},
    {"title": "The Reddits", "url": "reddits.html"},
    {"title": "How to Start Google", "url": "google.html"},
    {"title": "The Best Essay", "url": "best.html"},
    {"title": "Superlinear Returns", "url": "superlinear.html"},
    {"title": "How to Get New Ideas", "url": "getideas.html"},
    {"title": "The Need to Read", "url": "read.html"},
    {"title": "What You (Want to)* Want", "url": "want.html"},
    {"title": "Alien Truth", "url": "alien.html"},
    {"title": "What I've Learned from Users", "url": "users.html"},
    {"title": "Heresy", "url": "heresy.html"},
    {"title": "Putting Ideas into Words", "url": "words.html"},
    {"title": "Is There Such a Thing as Good Taste?", "url": "goodtaste.html"},
    {"title": "Beyond Smart", "url": "smart.html"},
    {"title": "Weird Languages", "url": "weird.html"},
    {"title": "How to Work Hard", "url": "hwh.html"},
    {"title": "A Project of One's Own", "url": "own.html"},
    {"title": "Fierce Nerds", "url": "fn.html"},
    {"title": "Crazy New Ideas", "url": "newideas.html"},
    {"title": "An NFT That Saves Lives", "url": "nft.html"},
    {"title": "The Real Reason to End the Death Penalty", "url": "real.html"},
    {"title": "How People Get Rich Now", "url": "richnow.html"},
    {"title": "Write Simply", "url": "simply.html"},
    {"title": "Donate Unrestricted", "url": "donate.html"},
    {"title": "What I Worked On", "url": "worked.html"},
    {"title": "Earnestness", "url": "earnest.html"},
    {"title": "Billionaires Build", "url": "ace.html"},
    {"title": "The Airbnbs", "url": "airbnbs.html"},
    {"title": "How to Think for Yourself", "url": "think.html"},
    {"title": "Early Work", "url": "early.html"},
    {"title": "Modeling a Wealth Tax", "url": "wtax.html"},
    {"title": "The Four Quadrants of Conformism", "url": "conformism.html"},
    {"title": "Orthodox Privilege", "url": "orth.html"},
    {"title": "Coronavirus and Credibility", "url": "cred.html"},
    {"title": "How to Write Usefully", "url": "useful.html"},
    {"title": "Being a Noob", "url": "noob.html"},
    {"title": "Haters", "url": "fh.html"},
    {"title": "The Two Kinds of Moderate", "url": "mod.html"},
    {"title": "Fashionable Problems", "url": "fp.html"},
    {"title": "The Lesson to Unlearn", "url": "lesson.html"},
    {"title": "Novelty and Heresy", "url": "nov.html"},
    {"title": "The Bus Ticket Theory of Genius", "url": "genius.html"},
    {"title": "General and Surprising", "url": "sun.html"},
    {"title": "Charisma / Power", "url": "pow.html"},
    {"title": "The Risk of Discovery", "url": "disc.html"},
    {"title": "How to Make Pittsburgh a Startup Hub", "url": "pgh.html"},
    {"title": "Life is Short", "url": "vb.html"},
    {"title": "Economic Inequality", "url": "ineq.html"},
    {"title": "The Refragmentation", "url": "re.html"},
    {"title": "Jessica Livingston", "url": "jessica.html"},
    {"title": "A Way to Detect Bias", "url": "bias.html"},
    {"title": "Write Like You Talk", "url": "talk.html"},
    {"title": "Default Alive or Default Dead?", "url": "aord.html"},
    {"title": "Why It's Safe for Founders to Be Nice", "url": "safe.html"},
    {"title": "Change Your Name", "url": "name.html"},
    {"title": "What Microsoft Is this the Altair Basic of?", "url": "altair.html"},
    {"title": "The Ronco Principle", "url": "ronco.html"},
    {"title": "What Doesn't Seem Like Work?", "url": "work.html"},
    {"title": "Don't Talk to Corp Dev", "url": "corpdev.html"},
    {"title": "Let the Other 95% of Great Programmers In", "url": "95.html"},
    {"title": "How to Be an Expert in a Changing World", "url": "ecw.html"},
    {"title": "How You Know", "url": "know.html"},
    {"title": "The Fatal Pinch", "url": "pinch.html"},
    {"title": "Mean People Fail", "url": "mean.html"},
    {"title": "Before the Startup", "url": "before.html"},
    {"title": "How to Raise Money", "url": "fr.html"},
    {"title": "Investor Herd Dynamics", "url": "herd.html"},
    {"title": "How to Convince Investors", "url": "convince.html"},
    {"title": "Do Things that Don't Scale", "url": "ds.html"},
    {"title": "Startup Investing Trends", "url": "invtrend.html"},
    {"title": "How to Get Startup Ideas", "url": "startupideas.html"},
    {"title": "The Hardware Renaissance", "url": "hw.html"},
    {"title": "Startup = Growth", "url": "growth.html"},
    {"title": "Black Swan Farming", "url": "swan.html"},
    {"title": "The Top of My Todo List", "url": "todo.html"},
    {"title": "Writing and Speaking", "url": "speak.html"},
    {"title": "How Y Combinator Started", "url": "ycstart.html"},
    {"title": "Defining Property", "url": "property.html"},
    {"title": "Frighteningly Ambitious Startup Ideas", "url": "ambitious.html"},
    {"title": "A Word to the Resourceful", "url": "word.html"},
    {"title": "Schlep Blindness", "url": "schlep.html"},
    {"title": "Snapshot: Viaweb, June 1998", "url": "vw.html"},
    {"title": "Why Startup Hubs Work", "url": "hubs.html"},
    {"title": "The Patent Pledge", "url": "patentpledge.html"},
    {"title": "Subject: Airbnb", "url": "airbnb.html"},
    {"title": "Founder Control", "url": "control.html"},
    {"title": "Tablets", "url": "tablets.html"},
    {"title": "What We Look for in Founders", "url": "founders.html"},
    {"title": "The New Funding Landscape", "url": "superangels.html"},
    {"title": "Where to See Silicon Valley", "url": "seesv.html"},
    {"title": "High Resolution Fundraising", "url": "hiresfund.html"},
    {"title": "What Happened to Yahoo", "url": "yahoo.html"},
    {"title": "The Future of Startup Funding", "url": "future.html"},
    {"title": "The Acceleration of Addictiveness", "url": "addiction.html"},
    {"title": "The Top Idea in Your Mind", "url": "top.html"},
    {"title": "Organic Startup Ideas", "url": "organic.html"},
    {"title": "Apple's Mistake", "url": "apple.html"},
    {"title": "What Startups Are Really Like", "url": "really.html"},
    {"title": "Persuade xor Discover", "url": "discover.html"},
    {"title": "Post-Medium Publishing", "url": "publishing.html"},
    {"title": "The List of N Things", "url": "nthings.html"},
    {"title": "The Anatomy of Determination", "url": "determination.html"},
    {"title": "What Kate Saw in Silicon Valley", "url": "kate.html"},
    {"title": "The Trouble with the Segway", "url": "segway.html"},
    {"title": "Ramen Profitable", "url": "ramenprofitable.html"},
    {"title": "Maker's Schedule, Manager's Schedule", "url": "makersschedule.html"},
    {"title": "A Local Revolution?", "url": "revolution.html"},
    {"title": "Why Twitter is a Big Deal", "url": "twitter.html"},
    {"title": "The Founder Visa", "url": "foundervisa.html"},
    {"title": "Five Founders", "url": "5founders.html"},
    {"title": "Relentlessly Resourceful", "url": "relres.html"},
    {"title": "How to Be an Angel Investor", "url": "angelinvesting.html"},
    {"title": "Why TV Lost", "url": "convergence.html"},
    {"title": "Can You Buy a Silicon Valley?  Maybe.", "url": "maybe.html"},
    {"title": "What I've Learned from Hacker News", "url": "hackernews.html"},
    {"title": "Startups in 13 Sentences", "url": "13sentences.html"},
    {"title": "Keep Your Identity Small", "url": "identity.html"},
    {"title": "After Credentials", "url": "credentials.html"},
    {"title": "Could VC be a Casualty of the Recession?", "url": "divergence.html"},
    {"title": "The High-Res Society", "url": "highres.html"},
    {"title": "The Other Half of \"Artists Ship\"", "url": "artistsship.html"},
    {"title": "Why to Start a Startup in a Bad Economy", "url": "badeconomy.html"},
    {"title": "A Fundraising Survival Guide", "url": "fundraising.html"},
    {"title": "The Pooled-Risk Company Management Company", "url": "prcmc.html"},
    {"title": "Cities and Ambition", "url": "cities.html"},
    {"title": "Disconnecting Distraction", "url": "distraction.html"},
    {"title": "Lies We Tell Kids", "url": "lies.html"},
    {"title": "Be Good", "url": "good.html"},
    {"title": "Why There Aren't More Googles", "url": "googles.html"},
    {"title": "Some Heroes", "url": "heroes.html"},
    {"title": "How to Disagree", "url": "disagree.html"},
    {"title": "You Weren't Meant to Have a Boss", "url": "boss.html"},
    {"title": "A New Venture Animal", "url": "ycombinator.html"},
    {"title": "Trolls", "url": "trolls.html"},
    {"title": "Six Principles for Making New Things", "url": "newthings.html"},
    {"title": "Why to Move to a Startup Hub", "url": "startuphubs.html"},
    {"title": "The Future of Web Startups", "url": "webstartups.html"},
    {"title": "How to Do Philosophy", "url": "philosophy.html"},
    {"title": "News from the Front", "url": "colleges.html"},
    {"title": "How Not to Die", "url": "die.html"},
    {"title": "Holding a Program in One's Head", "url": "head.html"},
    {"title": "Stuff", "url": "stuff.html"},
    {"title": "The Equity Equation", "url": "equity.html"},
    {"title": "An Alternative Theory of Unions", "url": "unions.html"},
    {"title": "The Hacker's Guide to Investors", "url": "guidetoinvestors.html"},
    {"title": "Two Kinds of Judgement", "url": "judgement.html"},
    {"title": "Microsoft is Dead", "url": "microsoft.html"},
    {"title": "Why to Not Not Start a Startup", "url": "notnot.html"},
    {"title": "Is It Worth Being Wise?", "url": "wisdom.html"},
    {"title": "Learning from Founders", "url": "foundersatwork.html"},
    {"title": "How Art Can Be Good", "url": "goodart.html"},
    {"title": "The 18 Mistakes That Kill Startups", "url": "startupmistakes.html"},
    {"title": "A Student's Guide to Startups", "url": "mit.html"},
    {"title": "How to Present to Investors", "url": "investors.html"},
    {"title": "Copy What You Like", "url": "copy.html"},
    {"title": "The Island Test", "url": "island.html"},
    {"title": "The Power of the Marginal", "url": "marginal.html"},
    {"title": "Why Startups Condense in America", "url": "america.html"},
    {"title": "How to Be Silicon Valley", "url": "siliconvalley.html"},
    {"title": "The Hardest Lessons for Startups to Learn", "url": "startuplessons.html"},
    {"title": "See Randomness", "url": "randomness.html"},
    {"title": "Are Software Patents Evil?", "url": "softwarepatents.html"},
    {"title": "6,631,372", "url": "6631327.html"},
    {"title": "Why YC", "url": "whyyc.html"},
    {"title": "How to Do What You Love", "url": "love.html"},
    {"title": "Good and Bad Procrastination", "url": "procrastination.html"},
    {"title": "Web 2.0", "url": "web20.html"},
    {"title": "How to Fund a Startup", "url": "startupfunding.html"},
    {"title": "The Venture Capital Squeeze", "url": "vcsqueeze.html"},
    {"title": "Ideas for Startups", "url": "ideas.html"},
    {"title": "What I Did this Summer", "url": "sfp.html"},
    {"title": "Inequality and Risk", "url": "inequality.html"},
    {"title": "After the Ladder", "url": "ladder.html"},
    {"title": "What Business Can Learn from Open Source", "url": "opensource.html"},
    {"title": "Hiring is Obsolete", "url": "hiring.html"},
    {"title": "The Submarine", "url": "submarine.html"},
    {"title": "Why Smart People Have Bad Ideas", "url": "bronze.html"},
    {"title": "Return of the Mac", "url": "mac.html"},
    {"title": "Writing,  Briefly", "url": "writing44.html"},
    {"title": "Undergraduation", "url": "college.html"},
    {"title": "A Unified Theory of VC Suckage", "url": "venturecapital.html"},
    {"title": "How to Start a Startup", "url": "start.html"},
    {"title": "What You'll Wish You'd Known", "url": "hs.html"},
    {"title": "Made in USA", "url": "usa.html"},
    {"title": "It's Charisma, Stupid", "url": "charisma.html"},
    {"title": "Bradley's Ghost", "url": "polls.html"},
    {"title": "A Version 1.0", "url": "laundry.html"},
    {"title": "What the Bubble Got Right", "url": "bubble.html"},
    {"title": "The Age of the Essay", "url": "essay.html"},
    {"title": "The Python Paradox", "url": "pypar.html"},
    {"title": "Great Hackers", "url": "gh.html"},
    {"title": "Mind the Gap", "url": "gap.html"},
    {"title": "How to Make Wealth", "url": "wealth.html"},
    {"title": "The Word \"Hacker\"", "url": "gba.html"},
    {"title": "What You Can't Say", "url": "say.html"},
    {"title": "Filters that Fight Back", "url": "ffb.html"},
    {"title": "Hackers and Painters", "url": "hp.html"},
    {"title": "If Lisp is So Great", "url": "iflisp.html"},
    {"title": "The Hundred-Year Language", "url": "hundred.html"},
    {"title": "Why Nerds are Unpopular", "url": "nerds.html"},
    {"title": "Better Bayesian Filtering", "url": "better.html"},
    {"title": "Design and Research", "url": "desres.html"},
    {"title": "A Plan for Spam", "url": "spam.html"},
    {"title": "Revenge of the Nerds", "url": "icad.html"},
    {"title": "Succinctness is Power", "url": "power.html"},
    {"title": "What Languages Fix", "url": "fix.html"},
    {"title": "Taste for Makers", "url": "taste.html"},
    {"title": "Why Arc Isn't Especially Object-Oriented", "url": "noop.html"},
    {"title": "What Made Lisp Different", "url": "diff.html"},
    {"title": "The Other Road Ahead", "url": "road.html"},
    {"title": "The Roots of Lisp", "url": "rootsoflisp.html"},
    {"title": "Five Questions about Language Design", "url": "langdes.html"},
    {"title": "Being Popular", "url": "popular.html"},
    {"title": "Java's Cover", "url": "javacover.html"},
    {"title": "Beating the Averages", "url": "avg.html"},
    {"title": "Lisp for Web-Based Applications", "url": "lwba.html"},
    {"title": "Programming Bottom-Up", "url": "progbot.html"},
    {"title": "This Year We Can End the Death Penalty in California", "url": "prop62.html"},
    {"title": "RSS", "url": "rss.html"}
]

def sanitize_filename(title):
    """파일명으로 사용할 수 있도록 제목을 정리합니다."""
    # 파일명에 사용할 수 없는 문자 제거
    filename = re.sub(r'[<>:"/\\|?*]', '', title)
    # 연속된 공백을 하나로
    filename = re.sub(r'\s+', ' ', filename)
    # 양쪽 공백 제거
    filename = filename.strip()
    # 공백을 언더스코어로 변경
    filename = filename.replace(' ', '_')
    # 최대 길이 제한
    if len(filename) > 100:
        filename = filename[:100]
    return filename

def scrape_essay(page, essay_url):
    """단일 에세이를 스크래핑합니다."""
    try:
        page.goto(f"https://paulgraham.com/{essay_url}", timeout=30000)
        time.sleep(0.5)  # 페이지 로딩 대기

        # 제목, 날짜, 내용 추출
        data = page.evaluate("""
            () => {
                const title = document.title;
                const contentCell = document.querySelector('table td[width="435"]');

                if (!contentCell) {
                    return { error: 'Content not found' };
                }

                const textContent = contentCell.textContent;
                const dateMatch = textContent.match(/(January|February|March|April|May|June|July|August|September|October|November|December)\\s+\\d{4}/);
                const date = dateMatch ? dateMatch[0] : '';

                const content = contentCell.innerText.trim();

                return { title, date, content };
            }
        """)

        return data
    except Exception as e:
        print(f"Error scraping {essay_url}: {str(e)}")
        return None

def save_essay_to_markdown(essay_data, filename):
    """에세이를 마크다운 파일로 저장합니다."""
    if not essay_data or 'error' in essay_data:
        return False

    markdown_content = f"""# {essay_data['title']}

**Date:** {essay_data['date']}

---

{essay_data['content']}
"""

    filepath = os.path.join('essays', f"{filename}.md")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    return True

def main():
    # essays 폴더 확인
    if not os.path.exists('essays'):
        os.makedirs('essays')

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        total = len(essays)
        successful = 0
        failed = 0

        print(f"Starting to scrape {total} essays...")

        for i, essay in enumerate(essays, 1):
            print(f"[{i}/{total}] Scraping: {essay['title']} ({essay['url']})")

            # 에세이 스크래핑
            essay_data = scrape_essay(page, essay['url'])

            if essay_data and 'error' not in essay_data:
                # 파일명 생성
                filename = sanitize_filename(essay['title'])

                # 마크다운 파일로 저장
                if save_essay_to_markdown(essay_data, filename):
                    successful += 1
                    print(f"  ✓ Saved as {filename}.md")
                else:
                    failed += 1
                    print(f"  ✗ Failed to save")
            else:
                failed += 1
                print(f"  ✗ Failed to scrape")

            # 서버 부하 방지를 위한 딜레이
            time.sleep(0.5)

        browser.close()

        print(f"\n=== Summary ===")
        print(f"Total essays: {total}")
        print(f"Successful: {successful}")
        print(f"Failed: {failed}")

if __name__ == "__main__":
    main()

import streamlit as st

st.html('''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>CourseRecommender-AI</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Poppins', sans-serif;
}

body{
    background:#000;
    color:white;
}

.container{
    width:100%;
    max-width:800px;
    margin:auto;
}

section{
    padding:25px;
}

.hero{
    min-height:35vh;
    display:flex;
    align-items:center;
    padding-top:20px;
    padding-bottom:20px;
}

.hero-content{
    max-width:650px;
}

.hero h1{
    font-size:clamp(2.5rem, 4vw, 5rem);
    margin-bottom:15px;
}

.hero p,
.built-for p,
.motivation-section p,
.research-section p{

    color:#cbd5e1;
    line-height:1.7;
    font-size:clamp(1rem, 2vw, 1.2rem);

}

.built-for h2,
.motivation-section h2,
.research-section h2{

    font-size:clamp(1.8rem, 3.5vw, 3rem);
    margin-bottom:10px;

}


.built-for,
.motivation-section,
.research-section{

    margin-top:15px;

}


.footer{

    max-width:800px;
    margin:auto;
    padding:25px;
    display:flex;
    justify-content:center;
    align-items:center;
    gap:30px;

}


.footer img{

    width:30px;
    height:30px;
    transition:0.3s;

}


.footer img:hover{

    transform:scale(1.2);

}


@media (max-width:768px){

    section{

        padding:20px;

    }


    .hero{

        min-height:30vh;

    }

}

</style>

</head>


<body>


<section class="hero">

    <div class="container hero-content">

        <h1>CourseRecommender</h1>

        <p>
            CourseRecommender AI is a Streamlit-based web application that helps
            users find relevant and trustworthy online courses through
            personalized recommendations.
        </p>

    </div>

</section>



<section class="built-for">

    <div class="container">

        <h2>Built for</h2>

        <p>
            CourseRecommender AI was built for students, lifelong learners,
            and professionals seeking new skills who want to learn through
            online courses while spending as little money as possible,
            or who feel overwhelmed among thousands of available options.
        </p>

    </div>

</section>



<section class="motivation-section">

    <div class="container">

        <h2>Why did I build CourseRecommender?</h2>

        <p>
            I created CourseRecommender because finding high-quality online
            courses can be overwhelming. There are thousands of options across
            multiple platforms, with varying prices and levels of quality.
            The goal of this project is to simplify that process and help
            learners discover courses that truly match their interests,
            objectives, and budget.
        </p>

    </div>

</section>



<section class="research-section">

    <div class="container">

        <h2>Privacy & Research</h2>

        <p>
            This project is currently being evaluated through a user study.
            Participation is voluntary, and responses are used exclusively
            for academic purposes. CourseRecommender-AI does not collect
            personal information through the application itself.
        </p>

    </div>

</section>



<footer class="footer">


    <a href="https://www.linkedin.com/in/felipe-fr/" target="_blank">

        <img src="https://res.cloudinary.com/r8yljzoc/image/upload/v1784051561/InBug-White_hdd6v1.png"
        alt="LinkedIn">

    </a>



    <a href="mailto:courserecommenderai@gmail.com">

        <img src="https://res.cloudinary.com/r8yljzoc/image/upload/v1784051560/Gmail_icon_2026_iotwot.webp"
        alt="Email">

    </a>



    <a href="https://github.com/felipe-f-rocha/CourseRecommender-AI" target="_blank">

        <img src="https://res.cloudinary.com/r8yljzoc/image/upload/v1784051560/github-logo_g0wodr.png"
        alt="Github">

    </a>


</footer>


</body>

</html>
''')
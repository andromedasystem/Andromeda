import React from 'react';
import { Grid, Image } from 'semantic-ui-react';

class Index extends React.Component {
    render() {
        // console.log(image_link);
        return <div>
                 <h3  style={{ marginBottom: '2em'}} className="ui center aligned header"> Admissions</h3>
                <Grid style={{ marginBottom: '5em !important'}}>
                    <Grid.Column width={6}>
                        <Image src='https://s3.amazonaws.com/andromeda-image-bucket/delfi-de-la-rua-140752-unsplash.jpg'/>
                    </Grid.Column>
                    <Grid.Column width={10}>
                        <p>We look forward to getting to know you through your application. Be sure to read all contents in this First-Year Admission section as well as the Application Instructions carefully before beginning an application.</p>

                        <p>Columbia accepts the Common Application or the Coalition Application; all first-year candidates must apply online. Columbia does not preference one application over the other; applicants should start and submit only one complete application. Questions specific to Columbia on each application are intended to obtain the same information.</p>

                        <p>We accept applications for Columbia College and Columbia Engineering, undergraduate divisions of Columbia University; both serve full-time students only. Potential applicants to Columbia College who have taken a break of more than a year in their educations (with the exception of those in mandatory military service) should consider instead Columbia University School of General Studies; the same is true for all students who wish to attend a part-time program because of personal or professional reasons.</p>
                    </Grid.Column>
                </Grid>
                <h3 className='ui center aligned header'  style={{ marginBottom: '2em'}}> Student Life</h3>
                <Grid  style={{ marginBottom: '5em !important'}}>
                    <Grid.Column width={10}>
                        <p>The college process is filled with numbers, statistics, worries, and stressors. Students often spend a lot of time researching a school’s admissions rates or financial aid policies, and while this information is certainly important, we often forget to worry about the quality of one’s life at a given school.
                            Whereas it might be easy to find out what percentage of applicants are accepted to a certain school, it can be harder to navigate the nuanced question of what an average day on a given campus might look like.</p>
                            <p>Columbia University is a prestigious school located in New York City. While you might have heard numerous facts, admissions stats, and rumors about this school, there is a lot more to it than just its selectivity and prestige. Read on to learn about the daily life of an average student at Columbia!</p>
                    </Grid.Column>
                    <Grid.Column width={6}>
                        <Image src='https://s3.amazonaws.com/andromeda-image-bucket/kyle-gregory-devaras-491943-unsplash.jpg'/>
                    </Grid.Column>
                </Grid>
                <h3 className='ui center aligned header' style={{ marginBottom: '2em'}}> About Us</h3>
                <Grid  style={{ marginBottom: '5em !important'}}>
                    <Grid.Column width={6}>
                        <Image src='https://s3.amazonaws.com/andromeda-image-bucket/davide-cantelli-153517-unsplash.jpg'/>
                    </Grid.Column>
                    <Grid.Column width={10}>
                        <p>Columbia University is one of the world's most important centers of research and at the same time a distinctive and distinguished learning environment for undergraduates and graduate students in many scholarly and professional fields.
                            The University recognizes the importance of its location in New York City and seeks to link its research and teaching to the vast resources of a great metropolis.</p>
                        <p>It seeks to attract a diverse and international faculty and student body, to support research and teaching on global issues, and to create academic relationships with many countries and regions. It expects all areas of the University to advance knowledge and learning at the highest level and to convey the products of its efforts to the world.</p>
                    </Grid.Column>
                </Grid>
                <h3 className='ui center aligned header'  style={{ marginBottom: '2em'}}>Alumni</h3>
                <Grid style={{ marginBottom: '5em !important'}}>
                    <Grid.Column width={10}>
                        <p>You're part of what makes SUNY Old Westbury a special place. Your experiences as a student, your memories of friends and faculty, and your ongoing loyalty to Old Westbury.</p>
                        <p>With each phase of your life, whether it is preparing to enter the workforce, starting a family, sending your child to college or beginning the golden years of your retirement, we want to be part of it – both in celebration and support. We are here to better serve your needs and interests. </p>
                        <p>No matter what year you graduated, you're a part of an alumni community that spans the globe — more than 24,000 strong.
                            Within these pages are a host of opportunities and tools to help alumni re-connect with each other and maintain close ties with Old Westbury.</p>
                        <p>Whether you graduated one year ago, 40 years ago, or sometime in between, you are invited to be part of our growing alumni network. Please share your expertise, time, and resources with your fellow and future graduates.</p>
                    </Grid.Column>
                    <Grid.Column width={6}>
                        <Image src='https://s3.amazonaws.com/andromeda-image-bucket/bench-accounting-49027-unsplash.jpg'/>
                    </Grid.Column>
                </Grid>
            </div>
    }
}

export default Index;

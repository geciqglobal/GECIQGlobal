from django.shortcuts import render, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView
from reportmaker.models import Article, Report, Tweet, RSS_Item, RSS_Feed, TK_Search, Twitter_User
from reportmaker import data_scan
import datetime as dt
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db.models import Q
import time

# Create your views here.
def home(request):
    context = {}
    try:
        report = Report.objects.get(report_date = dt.datetime.now())
        context['report_check'] = "Today's report has been created! No further action needed."
        context['report'] = report.get_absolute_url()
    except:
        context['report_check'] = "Today's report has not yet been created. Please go to the Report Making tool."
    return render(request, 'home.html', context = context)

def AllArticlesList(request):
    template = 'reportmaker/article_lists/all_articles_list.html'

    articles = Article.objects.filter( Q(archive = False) | (Q(archive = True) & Q(publication_date__gte=(dt.date.today() - dt.timedelta(days=1)))) )

    try:
        report = Report.objects.get(report_date = dt.date.today())
    except:
        return HttpResponseRedirect(reverse('reportmaker-redirect'))

    context = {'article_list': articles,}

    if request.method == "POST":
        article_id = request.POST.get('article_id')
        article_to_add = Article.objects.get(article_id = article_id)
        if 'add' in request.POST:
            article_to_add.report = report
            article_to_add.save()

            render(request, template, context = context)
            return HttpResponseRedirect(reverse('article-detail', args = [article_id]))

        elif 'remove' in request.POST:
            article_to_add.report = None
            article_to_add.archive = False
            article_to_add.save()
            return render(request, template, context = context)
    else:
        return render(request, template, context = context)

    return render(request, template, context = context)

def ChinaArticleList(request):
    template = 'reportmaker/article_lists/china_article_list.html'

    articles = Article.objects.filter(Q(search_focus = "china") & (Q(archive = False) | (Q(archive = True) & Q(publication_date__gte=(dt.date.today() - dt.timedelta(days=1))))) )
    try:
        report = Report.objects.get(report_date = dt.date.today())
    except:
        return HttpResponseRedirect(reverse('reportmaker-redirect'))
    context = {'article_list': articles, 'report': report}

    if request.method == "POST":
        article_id = request.POST.get('article_id')
        article_to_add = Article.objects.get(article_id = article_id)
        if 'add' in request.POST:
            article_to_add.report = report
            article_to_add.save()
            return HttpResponseRedirect(reverse('article-detail', args = [article_id]))
        elif 'remove' in request.POST:
            article_to_add.report = None
            article_to_add.archive = False
            article_to_add.save()
    else:
        return render(request, template, context = context)
    return render(request, template, context = context)

def IranArticleList(request):
    template = 'reportmaker/article_lists/iran_article_list.html'

    articles = Article.objects.filter(Q(search_focus = "iran") & (Q(archive = False) | (Q(archive = True) & Q(publication_date__gte=(dt.date.today() - dt.timedelta(days=1))))) )
    try:
        report = Report.objects.get(report_date = dt.date.today())
    except:
        return HttpResponseRedirect(reverse('reportmaker-redirect'))
    context = {'article_list': articles,}

    if request.method == "POST":
        article_id = request.POST.get('article_id')
        article_to_add = Article.objects.get(article_id = article_id)
        if 'add' in request.POST:
            article_to_add.report = report
            article_to_add.save()
            return HttpResponseRedirect(reverse('article-detail', args = [article_id]))
        elif 'remove' in request.POST:
            article_to_add.report = None
            article_to_add.archive = False
            article_to_add.save()
    else:
        return render(request, template, context = context)
    return render(request, template, context = context)

def RussiaArticleList(request):
    template = 'reportmaker/article_lists/russia_article_list.html'

    articles = Article.objects.filter(Q(search_focus = "russia") & (Q(archive = False) | (Q(archive = True) & Q(publication_date__gte=(dt.date.today() - dt.timedelta(days=1))))) )
    try:
        report = Report.objects.get(report_date = dt.date.today())
    except:
        return HttpResponseRedirect(reverse('reportmaker-redirect'))
    context = {'article_list': articles,}

    if request.method == "POST":
        article_id = request.POST.get('article_id')
        article_to_add = Article.objects.get(article_id = article_id)
        if 'add' in request.POST:
            article_to_add.report = report
            article_to_add.save()
            return HttpResponseRedirect(reverse('article-detail', args = [article_id]))
        elif 'remove' in request.POST:
            article_to_add.report = None
            article_to_add.archive = False
            article_to_add.save()
    else:
        return render(request, template, context = context)
    return render(request, template, context = context)

def CTArticleList(request):
    template = 'reportmaker/article_lists/ct_article_list.html'

    articles = Article.objects.filter(Q(search_focus = "ct") & (Q(archive = False) | (Q(archive = True) & Q(publication_date__gte=(dt.date.today() - dt.timedelta(days=1))))) )
    try:
        report = Report.objects.get(report_date = dt.date.today())
    except:
        return HttpResponseRedirect(reverse('reportmaker-redirect'))
    context = {'article_list': articles,}

    if request.method == "POST":
        article_id = request.POST.get('article_id')
        article_to_add = Article.objects.get(article_id = article_id)
        if 'add' in request.POST:
            article_to_add.report = report
            article_to_add.save()
            return HttpResponseRedirect(reverse('article-detail', args = [article_id]))
        elif 'remove' in request.POST:
            article_to_add.report = None
            article_to_add.archive = False
            article_to_add.save()
    else:
        return render(request, template, context = context)
    return render(request, template, context = context)

def EnvoyArticleList(request):
    template = 'reportmaker/article_lists/envoy_article_list.html'

    articles = Article.objects.filter(Q(search_focus = "envoy") & (Q(archive = False) | (Q(archive = True) & Q(publication_date__gte=(dt.date.today() - dt.timedelta(days=1))))) )
    try:
        report = Report.objects.get(report_date = dt.date.today())
    except:
        return HttpResponseRedirect(reverse('reportmaker-redirect'))
    context = {'article_list': articles,}

    if request.method == "POST":
        article_id = request.POST.get('article_id')
        article_to_add = Article.objects.get(article_id = article_id)
        if 'add' in request.POST:
            article_to_add.report = report
            article_to_add.save()
            return HttpResponseRedirect(reverse('article-detail', args = [article_id]))
        elif 'remove' in request.POST:
            article_to_add.report = None
            article_to_add.archive = False
            article_to_add.save()
    else:
        return render(request, template, context = context)
    return render(request, template, context = context)

def MetaArticleList(request):
    template = 'reportmaker/article_lists/meta_article_list.html'

    articles = Article.objects.filter(Q(search_focus = "meta") & (Q(archive = False) | (Q(archive = True) & Q(publication_date__gte=(dt.date.today() - dt.timedelta(days=1))))) )
    try:
        report = Report.objects.get(report_date = dt.date.today())
    except:
        return HttpResponseRedirect(reverse('reportmaker-redirect'))
    context = {'article_list': articles,}

    if request.method == "POST":
        article_id = request.POST.get('article_id')
        article_to_add = Article.objects.get(article_id = article_id)
        if 'add' in request.POST:
            article_to_add.report = report
            article_to_add.save()
            return HttpResponseRedirect(reverse('article-detail', args = [article_id]))
        elif 'remove' in request.POST:
            article_to_add.report = None
            article_to_add.archive = False
            article_to_add.save()
    else:
        return render(request, template, context = context)
    return render(request, template, context = context)

def TweetList(request):
    template = 'reportmaker/tweet_list.html'

    tweets = Tweet.objects.all()
    try:
        report = Report.objects.get(report_date = dt.date.today())
    except:
        return HttpResponseRedirect(reverse('reportmaker-redirect'))
    context = {'tweet_list': tweets,}

    if request.method == "POST":
        tweet_id = request.POST.get('tweet_id')
        tweet_to_add = Tweet.objects.get(tweet_id = tweet_id)
        if 'add' in request.POST:
            tweet_to_add.report = report
            tweet_to_add.save()
            return HttpResponseRedirect(reverse('tweet-detail', args = [tweet_id]))
        elif 'remove' in request.POST:
            tweet_to_add.report = None
            tweet_to_add.archive = False
            tweet_to_add.save()
    else:
        return render(request, template, context = context)
    return render(request, template, context = context)

def RSS_ItemList(request):
    template = 'reportmaker/rss_item_list.html'

    rss_items = RSS_Item.objects.all()
    try:
        report = Report.objects.get(report_date = dt.date.today())
    except:
        return HttpResponseRedirect(reverse('reportmaker-redirect'))
    context = {'rss_item_list': rss_items,}

    if request.method == "POST":
        rss_item_id = request.POST.get('rss_item_id')
        rss_item_to_add = RSS_Item.objects.get(rss_item_id = rss_item_id)
        if 'add' in request.POST:
            rss_item_to_add.report = report
            rss_item_to_add.save()
            return HttpResponseRedirect(reverse('rss-item-detail', args = [rss_item_id]))
        elif 'remove' in request.POST:
            rss_item_to_add.report = None
            rss_item_to_add.archive = False
            rss_item_to_add.save()
    else:
        return render(request, template, context = context)
    return render(request, template, context = context)

def DataScan(request):
    template = "reportmaker/article_refresh.html"

    if request.method == "POST":
        #Tweet.objects.filter(archive = False).delete()
        Article.objects.filter(archive = False).delete()
        RSS_Item.objects.filter(archive = False).delete()

        searches = TK_Search.objects.all()
        for search in searches:
            data_scan.get_tk_search(search.search_code, search.search_focus_descriptor, search.adversary_search)

        feeds = RSS_Feed.objects.all()
        for feed in feeds:
            try:
                data_scan.get_rss(feed.feed_url)
            except:
                print(feed.feed_url)

        #users = Twitter_User.objects.all()
        #for user in users:
            #data_scan.get_twitter(user.twitter_user_name)

        #This is a placeholder for an email alert in case of a Special Envoy/GEC related article
        if Article.objects.filter(archive = False, search_focus = "envoy").exists():
            print("Alert")

        return HttpResponseRedirect(reverse('article-list'))

    else:
        return render(request, template)

    return render(request, template)

class RSS_ItemDetailView(DetailView):
    model = RSS_Item

class RSS_ItemUpdateView(UpdateView):
    model = RSS_Item
    fields = "__all__"
    template_name_suffix = "_update_form"

class TweetDetailView(DetailView):
    model = Tweet

class TweetUpdateView(UpdateView):
    model = Tweet
    fields = [
        'tweet_text',
        'user',
        'retweet_count',
        ]
    template_name_suffix = '_update_form'

def ArticleDeleteAll(request):
    template = "reportmaker/article_clear.html"

    if request.method == "POST":
        Article.objects.all().delete()
        return HttpResponseRedirect(reverse('article-list'))

    else:
        return render(request, template)

    return render(request, template)

class ArticleDetailView(DetailView):
    model = Article

class ArticleUpdateView(UpdateView):
    model = Article
    fields = [
        'title',
        'article_text',
        'article_url',
        'adversary',
        ]
    template_name_suffix = '_update_form'

class ReportCreateView(CreateView):
    model = Report
    fields = ['report_date','report_intro',]

    def get_initial(self):
        today = dt.datetime.now()
        return {'report_date':today}

    def form_valid(self, form):
        same_day_reports = Report.objects.filter(report_date = dt.datetime.today()).delete()
        return super().form_valid(form)

class ReportUpdateView(UpdateView):
    model = Report
    fields = ['report_date','report_intro',]
    template_name_suffix = '_update_form'

def ReportView(request, pk):
    template = "reportmaker/report_detail.html"
    #note that this article count will produce a result that is slightly off after the email is sent
    article_count = Article.objects.filter(archive = False).count()
    tweet_count = Tweet.objects.filter(archive = False).count()
    report = get_object_or_404(Report, pk=pk)

    adversary_articles = Article.objects.filter(report = report, adversary = True)
    allied_articles = Article.objects.filter(report = report, adversary = False)
    rss_items = RSS_Item.objects.filter(report = report)

    context = {
        'report': report,
        'article_count': article_count,
        'tweet_count': tweet_count,
        'adversary_articles': adversary_articles,
        'allied_articles': allied_articles,
        'rss_items': rss_items
        }

    email_template = "reportmaker/updated_html_email.html"
    #email_template = "reportmaker/updated_email_template.html"

    if request.method == "POST":
        archived_articles = Article.objects.filter(report = report).update(archive = True)
        subject = "Special Envoy's Daily Brief" + str(dt.date.today())
        from_email = "constantin.sauvage@geciqglobal.com"
        to = [
            #"constantin.sauvage@accenturefederal.com",
            #"george.fleeson@accenturefederal.com",
            #"fleesong@state.gov",
            #"fleesongs@america.gov",
            #"sauvagecl@state.gov",
            ]

        html_content = render_to_string(email_template, context)
        text_content = strip_tags(html_content)

        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        report.sent = True
        report.save()

        return HttpResponseRedirect(reverse('home'))
    else:
        return render(request, template, context = context)
    return render(request, template, context = context)

class BootstrapEmailView(DetailView):
    model = Report
    template_name = "reportmaker/email_template.html"

    def get_context_data(self, **kwargs):
        context = super(BootstrapEmailView, self).get_context_data(**kwargs)

        article_count = Article.objects.filter(archive = False).count()
        tweet_count = Tweet.objects.filter(archive = False).count()
        adversary_articles = Article.objects.filter(report = self.object, adversary = True)
        allied_articles = Article.objects.filter(report = self.object, adversary = False)
        tweets = Tweet.objects.filter(report = self.object)
        rss_items = RSS_Item.objects.filter(report = self.object)

        context['adversary_articles'] = adversary_articles
        context['allied_articles'] = allied_articles
        context['tweets'] = tweets
        context['rss_items'] = rss_items
        context['article_count'] = article_count
        context['tweet_count'] = tweet_count
        return context

class HTMLEmailView(DetailView):
    model = Report
    template_name = "reportmaker/updated_html_email.html"
    #template_name = "reportmaker/updated_email_template.html"

    def get_context_data(self, **kwargs):
        context = super(HTMLEmailView, self).get_context_data(**kwargs)

        article_count = Article.objects.filter(archive = False).count()
        adversary_articles = Article.objects.filter(report = self.object, adversary = True)
        allied_articles = Article.objects.filter(report = self.object, adversary = False)
        rss_items = RSS_Item.objects.filter(report = self.object)
        pdf_date = self.object.report_date.strftime("%d%b%Y").upper()

        context['adversary_articles'] = adversary_articles
        context['allied_articles'] = allied_articles
        context['rss_items'] = rss_items
        context['article_count'] = article_count
        context['pdf_date'] = pdf_date
        return context

class ColorfulBootstrapEmailView(DetailView):
    model = Report
    template_name = "reportmaker/updated_email_template.html"

    def get_context_data(self, **kwargs):
        context = super(ColorfulBootstrapEmailView, self).get_context_data(**kwargs)

        article_count = Article.objects.filter(archive = False).count()
        tweet_count = Tweet.objects.filter(archive = False).count()
        adversary_articles = Article.objects.filter(report = self.object, adversary = True)
        allied_articles = Article.objects.filter(report = self.object, adversary = False)
        tweets = Tweet.objects.filter(report = self.object)
        rss_items = RSS_Item.objects.filter(report = self.object)

        context['adversary_articles'] = adversary_articles
        context['allied_articles'] = allied_articles
        context['tweets'] = tweets
        context['rss_items'] = rss_items
        context['article_count'] = article_count
        context['tweet_count'] = tweet_count
        return context

class ReportListView(ListView):
    model = Report

class ReportDeleteView(DeleteView):
    model = Report
    success_url = reverse_lazy('home')

def ReportMakerRedirect(request):
    template = "reportmaker/reportmaker_redirect.html"
    return render(request, template)

def TokenRefresher(request):
    template = "reportmaker/token_refresh.html"

    if request.method == "POST":
        data_scan.refresh_token()
        return HttpResponseRedirect(reverse('article-refresh'))

    else:
        return render(request, template)

    return render(request, template)

#hand jamming an article into the database and onto the report
class ArticleCreateView(CreateView):
    model = Article
    fields = [
        'title',
        'article_url',
        'publication_date',
        'author',
        'media_outlet',
        'search_focus',
        'article_text',
        'country',
        'adversary',
        ]

    def get_initial(self):
        today = dt.datetime.now()
        return {'publication_date': today}

    def form_valid(self, form):
        form.instance.readership = 0
        form.instance.link = "https://www.trendkite.com/"
        return super().form_valid(form)

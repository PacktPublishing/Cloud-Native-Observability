


# Cloud-Native Observability with OpenTelemetry

<a href="https://www.packtpub.com/cloud-networking/cloud-native-observability-with-opentelemetry?utm_source=github&utm_medium=repository&utm_campaign=9781801077705"><img src="https://static.packt-cdn.com/products/9781801077705/cover/smaller" alt="Cloud-Native Observability with OpenTelemetry" height="256px" align="right"></a>

This is the code repository for [Cloud-Native Observability with OpenTelemetry](https://www.packtpub.com/cloud-networking/cloud-native-observability-with-opentelemetry?utm_source=github&utm_medium=repository&utm_campaign=9781801077705), published by Packt.

**Learn to gain visibility into systems by combining tracing, metrics, and logging with OpenTelemetry**

## What is this book about?
Cloud-Native Observability with OpenTelemetry is a guide to helping you look for answers to questions about your applications. This book teaches you how to produce telemetry from your applications using an open standard to retain control of data. OpenTelemetry provides the tools necessary for you to gain visibility into the performance of your services. It allows you to instrument your application code through vendor-neutral APIs, libraries and tools. 

This book covers the following exciting features:
* Understand the core concepts of OpenTelemetry
* Explore concepts in distributed tracing, metrics, and logging
* Discover the APIs and SDKs necessary to instrument an application using OpenTelemetry
* Explore what auto-instrumentation is and how it can help accelerate application instrumentation
* Configure and deploy the OpenTelemetry Collector
Get to grips with how different open-source backends can be used to analyze telemetry data
Understand how to correlate telemetry in common scenarios to get to the root cause of a problem

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1801077703) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders. For example, Chapter02.

The code will look like the following:
```
from opentelemetry._metrics import set_meter_provider
from opentelemetry.sdk._metrics import MeterProvider
from opentelemetry.sdk.resources import Resource

def configure_meter_provider():
  provider = MeterProvider(resource=Resource.create())
  set_meter_provider(provider)

if __name__ == "__main__":
  configure_meter_provider()
```

**Following is what you need for this book:**
This book is for software engineers, library authors, and systems operators looking to better understand their infrastructure, services and applications by leveraging telemetry data like never before. Working knowledge of Python programming is assumed for the example applications that you’ll be building and instrumenting using the OpenTelemetry API and SDK. Some familiarity with Go programming, Linux, and Docker is preferable to help you set up additional components in various examples throughout the book.

With the following software and hardware list you can run all code files present in the book (Chapter 1-12).
### Software and Hardware List
| Chapter | Software required | OS required |
| -------- | ------------------------------------ | ----------------------------------- |
| 1-12 | OpenTelemetry for Python 1.9.0+ | Windows, Mac OS X, and Linux (Any) |
| 1-12 | OpenTelemetry Collector v0.42.0+ | Windows, Mac OS X, and Linux (Any) |

We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://static.packt-cdn.com/downloads/9781801077705_ColorImages.pdf).

<!-- 

-->
## Errata

* Page 29 (Figure 2.1): The port for the legacy-inventory should say **5001**
* Page 55 (Figure 2.5): The bubble between inventory API and inventory store should be labeled **4** instead of 3.

<!-- 

-->


### Related products
* Cloud Native with Kubernetes [[Packt]](https://www.packtpub.com/product/cloud-native-with-kubernetes/9781838823078?utm_source=github&utm_medium=repository&utm_campaign=9781838823078) [[Amazon]](https://www.amazon.com/dp/1838823077)

* The Kubernetes Bible [[Packt]](https://www.packtpub.com/product/the-kubernetes-bible/9781838827694?utm_source=github&utm_medium=repository&utm_campaign=9781838827694) [[Amazon]](https://www.amazon.com/dp/1838827692)

## Get to Know the Author
**Alex Boten**
is a senior staff software engineer at Lightstep and has spent the last 10 years
helping organizations adapt to a cloud-native landscape. From building core network
infrastructure to mobile client applications and everything in between, Alex has first-hand
knowledge of how complex troubleshooting distributed applications is.
This led him to the domain of observability and contributing to open source projects in
the space. A contributor, approver, and maintainer in several aspects of OpenTelemetry,
Alex has helped evolve the project from its early days in 2019 into the massive community
effort that it is today.
More than anything, Alex loves making sense of the technology around us and sharing his
learnings with others.
### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781801077705">https://packt.link/free-ebook/9781801077705 </a> </p>
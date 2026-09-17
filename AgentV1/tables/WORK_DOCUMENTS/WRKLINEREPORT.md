# DB2ADMIN.WRKLINEREPORT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 37
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 103562

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `EXPIRATIONDATE` | DATE |  |  |  |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 5 | `REPORTCODE` | CHAR(3) |  |  |  |  |
| 6 | `LINECODE` | CHAR(4) |  |  |  |  |
| 7 | `LONGDESCRIPTION` | VARCHAR(100) |  |  | description | Long human-readable label. |
| 8 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 9 | `LINETYPE` | CHAR(1) |  |  |  |  |
| 10 | `ALTERNATIVELINECODE` | CHAR(4) |  |  |  |  |
| 11 | `HUNDREDPERCENTLINE` | SMALLINT | NOT NULL |  |  |  |
| 12 | `DIMENSION` | CHAR(1) |  |  |  |  |
| 13 | `GLACCOUNTCODE` | CHAR(10) |  |  |  |  |
| 14 | `ACCOUNTTYPE` | CHAR(1) |  |  |  |  |
| 15 | `TIMESEGMENT` | CHAR(1) |  |  |  |  |
| 16 | `FISCALYEAR` | DECIMAL(4,0) |  |  |  |  |
| 17 | `MARKSHORTFISCALYEAR` | CHAR(1) |  |  |  |  |
| 18 | `PERIOD` | INTEGER | NOT NULL |  |  |  |
| 19 | `SUMMARIZATIONCODE` | CHAR(1) |  |  |  |  |
| 20 | `DIALOGCODE` | CHAR(1) |  |  |  |  |
| 21 | `INFOTYPECODE` | CHAR(2) |  |  |  |  |
| 22 | `VALUESEGMENTACTUAL` | DECIMAL(17,2) |  |  |  |  |
| 23 | `VALUESEGMENTPREVIOUS` | DECIMAL(17,2) |  |  |  |  |
| 24 | `OPENINGTOSEGMENTACTUAL` | DECIMAL(17,2) |  |  |  |  |
| 25 | `OPENINGTOSEGMENTPREVIOUS` | DECIMAL(17,2) |  |  |  |  |
| 26 | `OPENINGTOENDACTUAL` | DECIMAL(17,2) |  |  |  |  |
| 27 | `OPENINGTOENDPREVIOUS` | DECIMAL(17,2) |  |  |  |  |
| 28 | `OPENINGBALANCEACTUAL` | DECIMAL(17,2) |  |  |  |  |
| 29 | `INFOTYPECOMPARISONCODE` | CHAR(2) |  |  |  |  |
| 30 | `COMPVALUESEGMENTACTUAL` | DECIMAL(17,2) |  |  |  |  |
| 31 | `COMPVALUESEGMENTPREVIOUS` | DECIMAL(17,2) |  |  |  |  |
| 32 | `COMPOPENINGTOSEGMENTACTUAL` | DECIMAL(17,2) |  |  |  |  |
| 33 | `COMPOPENINGTOSEGMENTPREVIOUS` | DECIMAL(17,2) |  |  |  |  |
| 34 | `COMPOPENINGTOENDACTUAL` | DECIMAL(17,2) |  |  |  |  |
| 35 | `COMPOPENINGTOENDPREVIOUS` | DECIMAL(17,2) |  |  |  |  |
| 36 | `COMPOPENINGBALANCEACTUAL` | DECIMAL(17,2) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINE,
       t.EXPIRATIONDATE,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.REPORTCODE,
       t.LINECODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.LINETYPE,
       t.ALTERNATIVELINECODE,
       t.HUNDREDPERCENTLINE
FROM   DB2ADMIN.WRKLINEREPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

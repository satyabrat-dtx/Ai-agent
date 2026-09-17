# DB2ADMIN.CURRENCYBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `CORE_MASTER` (high confidence — table name starts with 'CURRENCY')
- **Roles**: `staging_mirror`
- **Columns**: 35
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 83344

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `CODE` | CHAR(4) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `ROUNDINGCRITERIATYPE` | CHAR(2) |  |  |  |  |
| 6 | `VALUEDECIMALNUMBER` | INTEGER | NOT NULL |  |  |  |
| 7 | `DIVISORFOREXCHANGERATE` | DECIMAL(11,0) |  |  |  |  |
| 8 | `TAXROUNDINGCRITERIATYPE` | CHAR(2) |  |  |  |  |
| 9 | `TAXVALUEDECIMALNUMBER` | INTEGER | NOT NULL |  |  |  |
| 10 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 11 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 12 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 13 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 14 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 15 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 16 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 17 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 18 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 19 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 20 | `TOLERANCECALCULATION` | DECIMAL(11,2) |  |  |  |  |
| 21 | `ADDITIONALTOLERANCECHECK` | SMALLINT | NOT NULL |  |  |  |
| 22 | `TOLERANCERATE` | DECIMAL(5,2) |  |  |  |  |
| 23 | `TOLERANCERECALCULATION` | DECIMAL(11,2) |  |  |  |  |
| 24 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 25 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 26 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 27 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 28 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 29 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 30 | `ISO4217` | CHAR(3) |  |  |  |  |
| 31 | `TOLERANCECALCULATIONRC` | DECIMAL(11,2) |  |  |  |  |
| 32 | `ADDITIONALTOLERANCECHECKRC` | SMALLINT | NOT NULL |  |  |  |
| 33 | `TOLERANCERATERC` | DECIMAL(5,2) |  |  |  |  |
| 34 | `TOLERANCERECALCULATIONRC` | DECIMAL(11,2) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CURRENCYBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ROUNDINGCRITERIATYPE,
       t.VALUEDECIMALNUMBER,
       t.DIVISORFOREXCHANGERATE,
       t.TAXROUNDINGCRITERIATYPE,
       t.TAXVALUEDECIMALNUMBER,
       t.WSOPERATION,
       t.IMPORTSTATUS
FROM   DB2ADMIN.CURRENCYBEAN t
FETCH FIRST 100 ROWS ONLY;
```

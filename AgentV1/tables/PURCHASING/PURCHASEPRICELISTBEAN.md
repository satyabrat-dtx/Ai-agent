# DB2ADMIN.PURCHASEPRICELISTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `staging_mirror`
- **Columns**: 44
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 93535

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 4 | `CODE` | CHAR(8) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `TEMPLATEDEFINITIONTYPE` | CHAR(1) |  |  |  |  |
| 6 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 7 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 8 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 9 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 10 | `INITIALDATE` | DATE |  |  |  |  |
| 11 | `FINALDATE` | DATE |  |  |  |  |
| 12 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 13 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 14 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 15 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 16 | `MAXPOSITIVEPRCFOREXCHANGERATE` | DECIMAL(5,2) |  |  |  |  |
| 17 | `MAXNEGATIVEPRCFOREXCHANGERATE` | DECIMAL(5,2) |  |  |  |  |
| 18 | `ALLOWDIFFERENCES` | SMALLINT | NOT NULL |  |  |  |
| 19 | `MAXPOSITIVEPRCFORDOCPRICE` | DECIMAL(5,2) |  |  |  |  |
| 20 | `MAXNEGATIVEPRCFORDOCPRICE` | DECIMAL(5,2) |  |  |  |  |
| 21 | `ALLOWCONVERSION` | SMALLINT | NOT NULL |  |  |  |
| 22 | `ORDERCATEGORYORDERTYPE` | CHAR(1) |  |  |  |  |
| 23 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 24 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 25 | `ORDERTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 26 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 27 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 28 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 29 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 30 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 31 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 32 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 33 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 34 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 35 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 36 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 37 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 38 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 39 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 40 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 41 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 42 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 43 | `OPPOSITEEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PURCHASEPRICELISTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.CODE,
       t.TEMPLATEDEFINITIONTYPE,
       t.TEMPLATECODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.INITIALDATE,
       t.FINALDATE
FROM   DB2ADMIN.PURCHASEPRICELISTBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

# DB2ADMIN.EXTOPPRICELISTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `SUBCONTRACTING` (medium confidence — table name starts with 'EXTOP')
- **Roles**: `staging_mirror`
- **Columns**: 39
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 98812

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
| 27 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 28 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 29 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 30 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 31 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 32 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 33 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 34 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 35 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 36 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 37 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 38 | `OPPOSITEEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EXTOPPRICELISTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

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
FROM   DB2ADMIN.EXTOPPRICELISTBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

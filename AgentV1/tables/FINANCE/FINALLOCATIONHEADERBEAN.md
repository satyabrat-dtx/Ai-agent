# DB2ADMIN.FINALLOCATIONHEADERBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `staging_mirror`
- **Columns**: 41
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 227159

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `CODE` | CHAR(8) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `MAINSEQUENCE` | DECIMAL(8,0) |  |  |  |  |
| 7 | `SUBSEQUENCE` | DECIMAL(8,0) |  |  |  |  |
| 8 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 9 | `PROFITCENTREPROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 10 | `COSTCENTRECOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 11 | `GLCODE` | CHAR(20) |  |  |  |  |
| 12 | `FIRSTSEGUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 13 | `FIRSTSEGCODE` | CHAR(10) |  |  |  |  |
| 14 | `SNDSEGUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 15 | `SECONDSEGCODE` | CHAR(10) |  |  |  |  |
| 16 | `THIRDSEGUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 17 | `THIRDSEGCODE` | CHAR(10) |  |  |  |  |
| 18 | `FRSEGUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 19 | `FOURTHSEGCODE` | CHAR(10) |  |  |  |  |
| 20 | `FIFTHSEGUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 21 | `FIFTHSEGCODE` | CHAR(10) |  |  |  |  |
| 22 | `SIXTHSEGUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 23 | `SIXTHSEGCODE` | CHAR(10) |  |  |  |  |
| 24 | `SESEGUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 25 | `SEVENTHSEGCODE` | CHAR(10) |  |  |  |  |
| 26 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
| 27 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 28 | `VALIDFLAG` | SMALLINT | NOT NULL |  |  |  |
| 29 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 30 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 31 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 32 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 33 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 34 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 35 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 36 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 37 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 38 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 39 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 40 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINALLOCATIONHEADERBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.MAINSEQUENCE,
       t.SUBSEQUENCE,
       t.BUSINESSUNITCODE,
       t.PROFITCENTREPROFITCENTERCODE,
       t.COSTCENTRECOSTCENTERCODE,
       t.GLCODE
FROM   DB2ADMIN.FINALLOCATIONHEADERBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

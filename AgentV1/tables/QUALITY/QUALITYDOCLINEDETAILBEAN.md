# DB2ADMIN.QUALITYDOCLINEDETAILBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `QUALITY` (high confidence — table name starts with 'QUALITY')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 32
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 107199

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `LINE` | INTEGER | NOT NULL |  |  |  |
| 3 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 4 | `TESTLINESTATUS` | INTEGER | NOT NULL |  |  |  |
| 5 | `CHARACTERISTICCODE` | CHAR(10) |  |  |  |  |
| 6 | `UOMCODE` | CHAR(3) |  |  |  |  |
| 7 | `INTERNALSPECIFICATIONCODE` | CHAR(10) |  |  |  |  |
| 8 | `ISOSPECIFICATIONCODE` | CHAR(10) |  |  |  |  |
| 9 | `SUBCODESTANDARD` | CHAR(50) |  |  |  |  |
| 10 | `VALUEBOOLEAN` | SMALLINT | NOT NULL |  |  |  |
| 11 | `VALUESTRING` | CHAR(50) |  |  |  |  |
| 12 | `VALUEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 13 | `STATUS` | CHAR(2) |  |  |  |  |
| 14 | `VALUEGROUPCODE` | CHAR(20) |  |  |  |  |
| 15 | `ANNOTATION` | VARCHAR(250) |  |  |  |  |
| 16 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 17 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 18 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 19 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 20 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 21 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 22 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 23 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 24 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 25 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 26 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 27 | `FORCEEMPTYVALUE` | SMALLINT | NOT NULL |  |  |  |
| 28 | `CANCELED` | SMALLINT | NOT NULL |  |  |  |
| 29 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 30 | `ISFROMAUTOCREATE` | SMALLINT | NOT NULL |  |  |  |
| 31 | `QUALITYREASONCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **QUALITYDOCLINE**.`ABSUNIQUEID` (high confidence — name = 'QUALITYDOCLINE' + known child suffix 'DETAIL')
  - JOIN predicate: `QUALITYDOCLINEDETAILBEAN.FATHERID = QUALITYDOCLINE.ABSUNIQUEID`

## Indexes

- `QUALITYDOCLINEDETAILBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.LINE,
       t.SEQUENCE,
       t.TESTLINESTATUS,
       t.CHARACTERISTICCODE,
       t.UOMCODE,
       t.INTERNALSPECIFICATIONCODE,
       t.ISOSPECIFICATIONCODE,
       t.SUBCODESTANDARD,
       t.VALUEBOOLEAN,
       t.VALUESTRING
FROM   DB2ADMIN.QUALITYDOCLINEDETAILBEAN t
FETCH FIRST 100 ROWS ONLY;
```

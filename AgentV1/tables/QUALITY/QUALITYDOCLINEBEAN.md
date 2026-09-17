# DB2ADMIN.QUALITYDOCLINEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `QUALITY` (high confidence — table name starts with 'QUALITY')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 43
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 107124

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
| 13 | `VALUEQUANTITY2` | DECIMAL(15,5) |  |  |  |  |
| 14 | `VALUEQUANTITY3` | DECIMAL(15,5) |  |  |  |  |
| 15 | `STATUS` | CHAR(2) |  |  |  |  |
| 16 | `VALUEGROUPCODE` | CHAR(20) |  |  |  |  |
| 17 | `REPETITIONNUMBER` | INTEGER | NOT NULL |  |  |  |
| 18 | `REPETITIONPERFORMED` | INTEGER | NOT NULL |  |  |  |
| 19 | `ANNOTATION` | VARCHAR(250) |  |  |  |  |
| 20 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 21 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 22 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 23 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 24 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 25 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 26 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 27 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 28 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 29 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 30 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 31 | `FORCEEMPTYVALUE` | SMALLINT | NOT NULL |  |  |  |
| 32 | `ADDITIONALLINE` | SMALLINT | NOT NULL |  |  |  |
| 33 | `CANCELED` | SMALLINT | NOT NULL |  |  |  |
| 34 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 35 | `GROUPCODE` | CHAR(3) |  |  |  |  |
| 36 | `DATATYPE` | CHAR(2) |  |  |  |  |
| 37 | `SKIPUPDATEFATHERSTATUS` | SMALLINT | NOT NULL |  |  |  |
| 38 | `ISFROMAUTOCREATE` | SMALLINT | NOT NULL |  |  |  |
| 39 | `QUALITYREASONCODE` | CHAR(3) |  |  |  |  |
| 40 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 41 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 42 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `QUALITYDOCLINEBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `QUALITYDOCLINEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

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
FROM   DB2ADMIN.QUALITYDOCLINEBEAN t
FETCH FIRST 100 ROWS ONLY;
```

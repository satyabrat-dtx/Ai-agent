# DB2ADMIN.PDMDB1BEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PDM` (medium confidence — table name starts with 'PDM')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 52
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 57539

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DBLINEN` | DECIMAL(5,0) |  |  |  |  |
| 3 | `DBANNUL` | CHAR(1) |  |  |  |  |
| 4 | `DBSTEPN` | DECIMAL(5,0) |  |  |  |  |
| 5 | `DBCOMGR` | CHAR(10) |  |  |  |  |
| 6 | `DBCDTRA` | CHAR(10) |  |  |  |  |
| 7 | `DBRECT1CODE` | CHAR(3) |  |  |  |  |
| 8 | `DBCITE1` | CHAR(15) |  |  |  |  |
| 9 | `DBVERN1` | CHAR(3) |  |  |  |  |
| 10 | `DBVERS1` | DECIMAL(3,0) |  |  |  |  |
| 11 | `DBCOLRL` | CHAR(1) |  |  |  |  |
| 12 | `DBCOLORUSERGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 13 | `DBCOLORCODE` | CHAR(10) |  |  |  |  |
| 14 | `DBSIZRL` | CHAR(1) |  |  |  |  |
| 15 | `DBCDSIZSIZESTYPECODE` | CHAR(3) |  |  |  |  |
| 16 | `DBCDSIZCODE` | CHAR(10) |  |  |  |  |
| 17 | `DBQTYRL` | CHAR(1) |  |  |  |  |
| 18 | `DBATKEYRL` | CHAR(1) |  |  |  |  |
| 19 | `DBUNITACODE` | CHAR(3) |  |  |  |  |
| 20 | `DBQUANT` | DECIMAL(9,5) |  |  |  |  |
| 21 | `DBCALIP` | DECIMAL(5,2) |  |  |  |  |
| 22 | `DBNOTEF` | VARCHAR(3000) |  |  |  |  |
| 23 | `DBCDKS1` | CHAR(10) |  |  |  |  |
| 24 | `DBCDKS2` | CHAR(10) |  |  |  |  |
| 25 | `DBCSORT` | DECIMAL(7,0) |  |  |  |  |
| 26 | `DBNUMED` | DECIMAL(29,9) |  |  |  |  |
| 27 | `DBALFAD` | CHAR(20) |  |  |  |  |
| 28 | `DBATRECTY` | CHAR(10) |  |  |  |  |
| 29 | `DBATTPREC` | DECIMAL(1,0) |  |  |  |  |
| 30 | `DBATCITEM` | CHAR(15) |  |  |  |  |
| 31 | `DBATVERNR` | CHAR(3) |  |  |  |  |
| 32 | `DBATVERST` | DECIMAL(3,0) |  |  |  |  |
| 33 | `DBATCDKE1` | CHAR(10) |  |  |  |  |
| 34 | `DBSOURC` | CHAR(1) |  |  |  |  |
| 35 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 36 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 37 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 38 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 39 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 40 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 41 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 42 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 43 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 44 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 45 | `DBFIXWA` | DECIMAL(12,5) |  |  |  |  |
| 46 | `DBLINKC` | CHAR(10) |  |  |  |  |
| 47 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 48 | `DBLINKEDCDSIZSIZESTYPECODE` | CHAR(3) |  |  |  |  |
| 49 | `DBLINKEDCDSIZCODE` | CHAR(10) |  |  |  |  |
| 50 | `DBLINKEDCOLORUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 51 | `DBLINKEDCOLORCODE` | CHAR(10) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `PDMDB1BEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `PDMDB1BEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.DBLINEN,
       t.DBANNUL,
       t.DBSTEPN,
       t.DBCOMGR,
       t.DBCDTRA,
       t.DBRECT1CODE,
       t.DBCITE1,
       t.DBVERN1,
       t.DBVERS1,
       t.DBCOLRL
FROM   DB2ADMIN.PDMDB1BEAN t
FETCH FIRST 100 ROWS ONLY;
```

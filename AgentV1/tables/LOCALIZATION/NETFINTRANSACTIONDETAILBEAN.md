# DB2ADMIN.NETFINTRANSACTIONDETAILBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'NET')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 53
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 219174

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `LINENUMBER` | DECIMAL(7,0) |  |  |  |  |
| 3 | `ITAXCODE` | CHAR(3) |  |  |  |  |
| 4 | `GLCODE` | CHAR(20) |  |  |  |  |
| 5 | `CREDITLINE` | SMALLINT | NOT NULL |  |  |  |
| 6 | `SLCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 7 | `SLCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 8 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 9 | `AMOUNTINDC` | DECIMAL(18,5) |  |  |  |  |
| 10 | `DOCUMENTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 11 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 12 | `AMOUNTINCC` | DECIMAL(18,5) |  |  |  |  |
| 13 | `COMPANYCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 14 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 15 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 16 | `COMMENTS` | VARCHAR(255) |  |  |  |  |
| 17 | `REFERENCETEXT1` | CHAR(50) |  |  |  |  |
| 18 | `REFERENCETEXT2` | CHAR(20) |  |  |  |  |
| 19 | `REFERENCETEXT3` | CHAR(20) |  |  |  |  |
| 20 | `REFERENCETEXT4` | CHAR(20) |  |  |  |  |
| 21 | `REFERENCETEXT5` | CHAR(20) |  |  |  |  |
| 22 | `FIRSTUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 23 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 24 | `SNDUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 25 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 26 | `THIRDUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 27 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 28 | `FRUSGRPUSGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 29 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 30 | `FIFTHUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 31 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 32 | `SIXTHUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 33 | `SIXTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 34 | `SEUSGRPUSGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 35 | `SEVENTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 36 | `REFERENCEAMT1` | DECIMAL(18,5) |  |  |  |  |
| 37 | `REFERENCEAMT2` | DECIMAL(18,5) |  |  |  |  |
| 38 | `REFERENCEAMT3` | DECIMAL(18,5) |  |  |  |  |
| 39 | `REFERENCEAMT4` | DECIMAL(18,5) |  |  |  |  |
| 40 | `REFERENCEAMT5` | DECIMAL(18,5) |  |  |  |  |
| 41 | `OPPOSITEEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 42 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 43 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 44 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 45 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 46 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 47 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 48 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 49 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 50 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 51 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 52 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `NETFINTRANSACTIONDETAILBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `NETFINTRNDETAILBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.LINENUMBER,
       t.ITAXCODE,
       t.GLCODE,
       t.CREDITLINE,
       t.SLCUSTOMERSUPPLIERTYPE,
       t.SLCUSTOMERSUPPLIERCODE,
       t.ENTITYNAME,
       t.AMOUNTINDC,
       t.DOCUMENTCURRENCYCODE,
       t.EXCHANGERATE
FROM   DB2ADMIN.NETFINTRANSACTIONDETAILBEAN t
FETCH FIRST 100 ROWS ONLY;
```

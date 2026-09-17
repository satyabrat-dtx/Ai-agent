# DB2ADMIN.BOMCOMPONENTALTERNATIVEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'BOM')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 50
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 208164

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `ITEMNATURE` | CHAR(1) |  |  |  |  |
| 3 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 4 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 5 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 6 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 7 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 8 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `PRODUCTIONRESERVATIONGROUPCODE` | CHAR(3) |  |  |  |  |
| 18 | `PRODRESERVATIONLINKGROUPCODE` | CHAR(20) |  |  |  |  |
| 19 | `RESERVATIONWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 20 | `PRODUCTIONITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 21 | `ROUTINGNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 22 | `RTGSUBCODE01` | CHAR(20) |  |  |  |  |
| 23 | `RTGVIRTUALRETURNSUBCODE` | CHAR(30) |  |  |  |  |
| 24 | `RTGSUBCODE02` | CHAR(10) |  |  |  |  |
| 25 | `RTGSUBCODE03` | CHAR(10) |  |  |  |  |
| 26 | `RTGSUBCODE04` | CHAR(10) |  |  |  |  |
| 27 | `RTGSUBCODE05` | CHAR(10) |  |  |  |  |
| 28 | `RTGSUBCODE06` | CHAR(10) |  |  |  |  |
| 29 | `RTGSUBCODE07` | CHAR(10) |  |  |  |  |
| 30 | `RTGSUBCODE08` | CHAR(10) |  |  |  |  |
| 31 | `RTGSUBCODE09` | CHAR(10) |  |  |  |  |
| 32 | `RTGSUBCODE10` | CHAR(10) |  |  |  |  |
| 33 | `RTGSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 34 | `PLANNINGAVLWAREHOUSEGROUPCODE` | CHAR(3) |  |  |  |  |
| 35 | `PLANNINGAVLFORMULACODE` | CHAR(3) |  |  |  |  |
| 36 | `PLANNINGBALANCEFORMULACODE` | CHAR(3) |  |  |  |  |
| 37 | `IDENTIFIERALLALTERNATIVE` | VARCHAR(200) |  |  |  |  |
| 38 | `RTGFULLITEMCODE` | VARCHAR(120) |  |  |  |  |
| 39 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 40 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 41 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 42 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 43 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 44 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 45 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 46 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 47 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 48 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 49 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `BOMCOMPONENTALTERNATIVEBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `BOMCMPALTERNATIVEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.ITEMNATURE,
       t.ITEMTYPEAFICODE,
       t.PROTOTYPE,
       t.PROTOTYPEPROJECT,
       t.PROTOTYPEVERSION,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05
FROM   DB2ADMIN.BOMCOMPONENTALTERNATIVEBEAN t
FETCH FIRST 100 ROWS ONLY;
```

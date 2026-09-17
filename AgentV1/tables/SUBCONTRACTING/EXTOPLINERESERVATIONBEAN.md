# DB2ADMIN.EXTOPLINERESERVATIONBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `SUBCONTRACTING` (medium confidence — table name starts with 'EXTOP')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 41
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 235890

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `RESERVATIONORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 3 | `RESERVATIONORDERCODE` | CHAR(15) |  |  |  |  |
| 4 | `RESERVATIONRESERVATIONLINE` | DECIMAL(7,0) |  |  |  |  |
| 5 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 6 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 7 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |
| 17 | `VARIANTCODE` | CHAR(20) |  |  |  |  |
| 18 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 19 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 20 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 21 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 22 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 23 | `USEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 24 | `LATESTALLOCATIONDATE` | DATE |  |  |  |  |
| 25 | `ACTUALPICKUPDATE` | DATE |  |  |  |  |
| 26 | `FULLITEMDESCRIPTION` | CHAR(200) |  |  |  |  |
| 27 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 28 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 29 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 30 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 31 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 32 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 33 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 34 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 35 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 36 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 37 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 38 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 39 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 40 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **EXTOPLINE**.`ABSUNIQUEID` (medium confidence — name = 'EXTOPLINE' + recurring fragment 'RESERVATION' (seen in 6 tables))
  - JOIN predicate: `EXTOPLINERESERVATIONBEAN.FATHERID = EXTOPLINE.ABSUNIQUEID`

## Indexes

- `EXTOPLINERESERVATIONBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.RESERVATIONORDERCOUNTERCODE,
       t.RESERVATIONORDERCODE,
       t.RESERVATIONRESERVATIONLINE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06
FROM   DB2ADMIN.EXTOPLINERESERVATIONBEAN t
FETCH FIRST 100 ROWS ONLY;
```

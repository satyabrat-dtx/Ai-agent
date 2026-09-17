# DB2ADMIN.SALESORDERASSORTMENTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `SALES` (high confidence — table name starts with 'SALESORDER')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 48
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 59941

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `LINECREATED` | SMALLINT | NOT NULL |  |  |  |
| 3 | `NUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 4 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 5 | `SEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 6 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
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
| 17 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 18 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 19 | `CREATIONTYPE` | CHAR(1) |  |  |  |  |
| 20 | `ORDERUSERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 21 | `ORDERUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 22 | `ORDERBASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 23 | `ORDERBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 24 | `ORDERUSERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 25 | `ORDERUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 26 | `ORDERBASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 27 | `ORDERBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 28 | `ORDERUSERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 29 | `ORDERUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 30 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 31 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 32 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 33 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 34 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 35 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 36 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 37 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 38 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 39 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 40 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 41 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 42 | `SECQTYNOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 43 | `PACKQTYNOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 44 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 45 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 46 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 47 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **SALESORDER**.`ABSUNIQUEID` (high confidence — name = 'SALESORDER' + known child suffix 'ASSORTMENT')
  - JOIN predicate: `SALESORDERASSORTMENTBEAN.FATHERID = SALESORDER.ABSUNIQUEID`

## Indexes

- `SALESORDERASSORTMENTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.LINECREATED,
       t.NUMBERID,
       t.LINETEMPLATECODE,
       t.SEQUENCE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05
FROM   DB2ADMIN.SALESORDERASSORTMENTBEAN t
FETCH FIRST 100 ROWS ONLY;
```

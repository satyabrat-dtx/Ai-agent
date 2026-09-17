# DB2ADMIN.WAREHOUSEITEMCOSTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `WAREHOUSE` (high confidence — table name starts with 'WAREHOUSE')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 61
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 81380

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `WAREHOUSEACCOUNTINGGROUPCODE` | CHAR(3) |  |  |  |  |
| 4 | `COSTIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
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
| 16 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 17 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 18 | `LASTINBOUNDCOST` | DECIMAL(18,5) |  |  |  |  |
| 19 | `LASTINBOUNDCOSTLASTUPDATEDATE` | DATE |  |  |  |  |
| 20 | `STANDARDCOST` | DECIMAL(18,5) |  |  |  |  |
| 21 | `STANDARDCOSTLASTUPDATEDATE` | DATE |  |  |  |  |
| 22 | `WEIGHTEDAVERAGECOST` | DECIMAL(18,5) |  |  |  |  |
| 23 | `BASECOSTUNITCODE` | CHAR(3) |  |  |  |  |
| 24 | `DYNAMICAVERAGECOSTTOTALVALUE` | DECIMAL(18,5) |  |  |  |  |
| 25 | `DYNAMICAVERAGECOSTTOTALQTY` | DECIMAL(15,5) |  |  |  |  |
| 26 | `DYNAMICAVERAGECOSTUNITVALUE` | DECIMAL(18,5) |  |  |  |  |
| 27 | `HIFOCOST` | DECIMAL(18,5) |  |  |  |  |
| 28 | `HIFOCOSTLASTUPDATEDATE` | DATE |  |  |  |  |
| 29 | `SECONDSTANDARDCOST` | DECIMAL(18,5) |  |  |  |  |
| 30 | `SNDSTANDARDCOSTLASTUPDATEDATE` | DATE |  |  |  |  |
| 31 | `CORFQTY` | SMALLINT | NOT NULL |  |  |  |
| 32 | `CORFCOL` | SMALLINT | NOT NULL |  |  |  |
| 33 | `CORFSIZ` | SMALLINT | NOT NULL |  |  |  |
| 34 | `COFLCSA` | DECIMAL(15,5) |  |  |  |  |
| 35 | `COFLCSB` | DECIMAL(15,5) |  |  |  |  |
| 36 | `COFLCSC` | DECIMAL(15,5) |  |  |  |  |
| 37 | `STANDARDCOSTPERIOD` | DECIMAL(18,5) |  |  |  |  |
| 38 | `SECONDSTANDARDCOSTPERIOD` | DECIMAL(18,5) |  |  |  |  |
| 39 | `DEVALUEDSTANDARDCOST` | DECIMAL(18,5) |  |  |  |  |
| 40 | `DEVALUEDSECONDSTANDARDCOST` | DECIMAL(18,5) |  |  |  |  |
| 41 | `FINALPERIODDATE` | DATE |  |  |  |  |
| 42 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 43 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 44 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 45 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 46 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 47 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 48 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 49 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 50 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 51 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 52 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 53 | `LASTINBOUNDCOSTSNDCUR` | DECIMAL(18,5) |  |  |  |  |
| 54 | `WEIGHTEDAVERAGECOSTSNDCUR` | DECIMAL(18,5) |  |  |  |  |
| 55 | `DYNAMICAVERAGECOSTTOTVALSNDCUR` | DECIMAL(18,5) |  |  |  |  |
| 56 | `DYNAMICAVERAGECOSTUNITVLSNDCUR` | DECIMAL(18,5) |  |  |  |  |
| 57 | `HIFOCOSTSNDCUR` | DECIMAL(18,5) |  |  |  |  |
| 58 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 59 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 60 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `WAREHOUSEITEMCOSTBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `WAREHOUSEITEMCOSTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.WAREHOUSEACCOUNTINGGROUPCODE,
       t.COSTIDENTIFIER,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06
FROM   DB2ADMIN.WAREHOUSEITEMCOSTBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

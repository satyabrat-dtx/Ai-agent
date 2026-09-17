# DB2ADMIN.STOCKTAKEBALANCEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `INVENTORY` (high confidence — table name starts with 'STOCK')
- **Roles**: `staging_mirror`
- **Columns**: 67
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 107356

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `STOCKTAKEIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 3 | `STOCKTAKEIDENTIFIERLINE` | INTEGER | NOT NULL |  |  |  |
| 4 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 5 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 6 | `DECOSUBCODE01` | CHAR(20) |  |  |  |  |
| 7 | `DECOSUBCODE02` | CHAR(10) |  |  |  |  |
| 8 | `DECOSUBCODE03` | CHAR(10) |  |  |  |  |
| 9 | `DECOSUBCODE04` | CHAR(10) |  |  |  |  |
| 10 | `DECOSUBCODE05` | CHAR(10) |  |  |  |  |
| 11 | `DECOSUBCODE06` | CHAR(10) |  |  |  |  |
| 12 | `DECOSUBCODE07` | CHAR(10) |  |  |  |  |
| 13 | `DECOSUBCODE08` | CHAR(10) |  |  |  |  |
| 14 | `DECOSUBCODE09` | CHAR(10) |  |  |  |  |
| 15 | `DECOSUBCODE10` | CHAR(10) |  |  |  |  |
| 16 | `PHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 17 | `WHSLOCATIONWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 18 | `WAREHOUSELOCATIONCODE` | CHAR(10) |  |  |  |  |
| 19 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 20 | `LOTCODE` | CHAR(35) |  |  |  |  |
| 21 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 22 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 23 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 24 | `ELEMENTSSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 25 | `ELEMENTSCODE` | CHAR(15) |  |  |  |  |
| 26 | `LISTNUMBER` | DECIMAL(11,0) |  |  |  |  |
| 27 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 28 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 29 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 30 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 31 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 32 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 33 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 34 | `BASEPRIMARYUNITCODE` | CHAR(3) |  |  |  |  |
| 35 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 36 | `BASESECONDARYUNITCODE` | CHAR(3) |  |  |  |  |
| 37 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 38 | `PACKAGINGCODE` | CHAR(3) |  |  |  |  |
| 39 | `PACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 40 | `BASEPRIMARYQUANTITYVERIFIED` | DECIMAL(15,5) |  |  |  |  |
| 41 | `BASESECONDARYQUANTITYVERIFIED` | DECIMAL(15,5) |  |  |  |  |
| 42 | `PACKAGINGQUANTITYVERIFIED` | DECIMAL(15,5) |  |  |  |  |
| 43 | `VERIFIEDLOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 44 | `VERIFIEDPHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 45 | `VERIFIEDWHSLOCWHSZONECODE` | CHAR(3) |  |  |  |  |
| 46 | `VERIFIEDWAREHOUSELOCATIONCODE` | CHAR(10) |  |  |  |  |
| 47 | `VERIFIEDCONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 48 | `VERIFIEDCONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 49 | `VERIFIEDCONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 50 | `TRANSFERMISSINGQUANTITY` | SMALLINT | NOT NULL |  |  |  |
| 51 | `VERIFIEDLINE` | SMALLINT | NOT NULL |  |  |  |
| 52 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 53 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 54 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 55 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 56 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 57 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 58 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 59 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 60 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 61 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 62 | `ISNEWELEMENT` | SMALLINT | NOT NULL |  |  |  |
| 63 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 64 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 65 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 66 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `STOCKTAKEBALANCEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.STOCKTAKEIDENTIFIER,
       t.STOCKTAKEIDENTIFIERLINE,
       t.ITEMTYPECODE,
       t.LOGICALWAREHOUSECODE,
       t.DECOSUBCODE01,
       t.DECOSUBCODE02,
       t.DECOSUBCODE03,
       t.DECOSUBCODE04,
       t.DECOSUBCODE05,
       t.DECOSUBCODE06
FROM   DB2ADMIN.STOCKTAKEBALANCEBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

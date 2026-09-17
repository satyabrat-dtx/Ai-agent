# DB2ADMIN.ITEMREPLENISHMENTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'ITEM')
- **Roles**: `staging_mirror`
- **Columns**: 73
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 89903

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 3 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 4 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 5 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 6 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 7 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `WHSREPLENISHMENTGROUPCODE` | CHAR(3) |  |  |  |  |
| 14 | `PLANNINGTYPE` | CHAR(2) |  |  |  |  |
| 15 | `TERMSOFPLANNING` | CHAR(2) |  |  |  |  |
| 16 | `PLANNERCODE` | CHAR(50) |  |  |  |  |
| 17 | `MAINREPLENISHMENTTYPE` | CHAR(2) |  |  |  |  |
| 18 | `PRIMARYLOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 19 | `TRANSFERLOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 20 | `DRPLOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 21 | `USUALSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 22 | `USUALSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 23 | `USUALSUBCONTRACTORTYPE` | CHAR(1) |  |  |  |  |
| 24 | `USUALSUBCONTRACTORCODE` | CHAR(8) |  |  |  |  |
| 25 | `REQUISITIONTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 26 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 27 | `BASEPRIMARYUNITCODE` | CHAR(3) |  |  |  |  |
| 28 | `SUPPLIERORDERLOWERQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 29 | `PRODUCTIONORDERLOWERQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 30 | `SBCORDERLOWERQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 31 | `INTERNALORDERLOWERQUANTITYTO` | DECIMAL(15,5) |  |  |  |  |
| 32 | `INTERNALORDERLOWERQUANTITYFROM` | DECIMAL(15,5) |  |  |  |  |
| 33 | `DIRTYFIELD` | CHAR(20) |  |  |  |  |
| 34 | `TOTALLEADTIME` | DECIMAL(5,2) |  |  |  |  |
| 35 | `CALCDATETOTALLEADTIME` | DATE |  |  |  |  |
| 36 | `PRODUCTIONFIXEDLEADTIME` | DECIMAL(5,2) |  |  |  |  |
| 37 | `PRODUCTIONVARIABLELEADTIME` | DECIMAL(5,2) |  |  |  |  |
| 38 | `PURCHASELEADTIME` | DECIMAL(5,2) |  |  |  |  |
| 39 | `SUBCONTRACTORFIXEDLEADTIME` | DECIMAL(5,2) |  |  |  |  |
| 40 | `SUBCONTRACTORVARIABLELEADTIME` | DECIMAL(5,2) |  |  |  |  |
| 41 | `SESSIONSTEP` | CHAR(2) |  |  |  |  |
| 42 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 43 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 44 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 45 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 46 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 47 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 48 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 49 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 50 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 51 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 52 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 53 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 54 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 55 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 56 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 57 | `REORDERPOINT` | DECIMAL(15,5) |  |  |  |  |
| 58 | `SAFETYSTOCK` | DECIMAL(15,5) |  |  |  |  |
| 59 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 60 | `SUPPLIERQUANTITYINCREMENTS` | DECIMAL(15,5) |  |  |  |  |
| 61 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 62 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 63 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 64 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 65 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 66 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 67 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 68 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |
| 69 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 70 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 71 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 72 | `PRODUCTIONDEMANDTEMPLATECODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ITEMREPLENISHMENTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08,
       t.SUBCODE09
FROM   DB2ADMIN.ITEMREPLENISHMENTBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

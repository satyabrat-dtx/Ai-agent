# DB2ADMIN.WRKUSAPRODUCTIONORDERPRINT2

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 81
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 115621

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `EXPIRATIONDATE` | DATE |  |  |  |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 5 | `PRODUCTIONDEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 6 | `PRODUCTIONDEMANDCODE` | CHAR(15) |  |  |  |  |
| 7 | `RLORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 8 | `RLORDERCODE` | CHAR(15) |  |  |  |  |
| 9 | `RLRESERVATIONLINE` | DECIMAL(5,0) |  |  |  |  |
| 10 | `GROUPSTEPNUMBER` | INTEGER | NOT NULL |  |  |  |
| 11 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 12 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 13 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 14 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 24 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 25 | `USEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 26 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 27 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 28 | `USEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 29 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 30 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 31 | `USEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 32 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 33 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 34 | `USEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 35 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 36 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 37 | `USEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 38 | `ALLOCATIONCODE` | CHAR(15) |  |  |  |  |
| 39 | `ALLOCATIONLINENUMBER` | DECIMAL(5,0) |  |  |  |  |
| 40 | `ALLOCATIONCOMPONENTLINENUMBER` | DECIMAL(5,0) |  |  |  |  |
| 41 | `ALLOCATEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 42 | `ALLOCATEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 43 | `ALLOCATEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 44 | `ALLOCATEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 45 | `ALLOCATEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 46 | `STTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 47 | `STTRANSACTIONDETAILNUMBER` | INTEGER |  |  |  |  |
| 48 | `ISSUEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 49 | `ISSUEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 50 | `ISSUEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 51 | `ISSUEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 52 | `ISSUEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 53 | `ISSUEWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 54 | `ORIGINALCREATIONTIMESTAMP` | BIGINT | NOT NULL |  |  |  |
| 55 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 56 | `PHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 57 | `WHSLOCATIONWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 58 | `WAREHOUSELOCATIONCODE` | CHAR(10) |  |  |  |  |
| 59 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 60 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 61 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 62 | `LOTCODE` | CHAR(10) |  |  |  |  |
| 63 | `ITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 64 | `ITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 65 | `NUMBERFIELD1` | DECIMAL(15,5) |  |  |  |  |
| 66 | `NUMBERFIELD2` | DECIMAL(15,5) |  |  |  |  |
| 67 | `NUMBERFIELD3` | DECIMAL(15,5) |  |  |  |  |
| 68 | `NUMBERFIELD4` | DECIMAL(15,5) |  |  |  |  |
| 69 | `NUMBERFIELD5` | DECIMAL(15,5) |  |  |  |  |
| 70 | `CHARFIELD1` | CHAR(50) |  |  |  |  |
| 71 | `CHARFIELD2` | CHAR(50) |  |  |  |  |
| 72 | `CHARFIELD3` | CHAR(50) |  |  |  |  |
| 73 | `CHARFIELD4` | CHAR(50) |  |  |  |  |
| 74 | `CHARFIELD5` | CHAR(50) |  |  |  |  |
| 75 | `DATEFIELD1` | DATE |  |  |  |  |
| 76 | `DATEFIELD2` | DATE |  |  |  |  |
| 77 | `DATEFIELD3` | DATE |  |  |  |  |
| 78 | `INTFIELD1` | INTEGER | NOT NULL |  |  |  |
| 79 | `INTFIELD2` | INTEGER | NOT NULL |  |  |  |
| 80 | `INTFIELD3` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINE,
       t.EXPIRATIONDATE,
       t.COMPANYCODE,
       t.PRODUCTIONORDERCODE,
       t.PRODUCTIONDEMANDCOUNTERCODE,
       t.PRODUCTIONDEMANDCODE,
       t.RLORDERCOUNTERCODE,
       t.RLORDERCODE,
       t.RLRESERVATIONLINE,
       t.GROUPSTEPNUMBER,
       t.WAREHOUSECODE
FROM   DB2ADMIN.WRKUSAPRODUCTIONORDERPRINT2 t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

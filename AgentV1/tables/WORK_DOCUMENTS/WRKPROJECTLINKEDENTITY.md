# DB2ADMIN.WRKPROJECTLINKEDENTITY

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 58
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 197849

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CHOOSE` | SMALLINT | NOT NULL |  |  |  |
| 1 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |
| 2 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 3 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 4 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `HASERRORS` | SMALLINT | NOT NULL |  |  |  |
| 6 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 7 | `ERRORMESSAGE` | VARCHAR(250) |  |  |  |  |
| 8 | `ENTITYTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `ENTITYDATE` | DATE |  |  |  |  |
| 10 | `ENTITYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 11 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
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
| 23 | `PRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 24 | `PRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 25 | `SECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 26 | `SECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 27 | `PACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 28 | `PACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 29 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 30 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 31 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 32 | `ISSUETEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 33 | `ISSUETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 34 | `ENTRYTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 35 | `ENTRYTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 36 | `SODORDLINSALESORDERCODE` | CHAR(8) |  |  |  |  |
| 37 | `SODORDLINORDERLINE` | CHAR(15) |  |  |  |  |
| 38 | `SODORDLINORDERSUBLINE` | DECIMAL(7,0) |  |  |  |  |
| 39 | `SODORDLINCOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 40 | `SODDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 41 | `SALESORDERDELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 42 | `SALESRELEASELINECODE` | CHAR(15) |  |  |  |  |
| 43 | `SALESRELEASELINELINE` | DECIMAL(7,0) |  |  |  |  |
| 44 | `SALESRELEASELINESUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 45 | `SALRELEASELINECMPRELEASELINE` | DECIMAL(3,0) |  |  |  |  |
| 46 | `PODORDLINSALESORDERCODE` | CHAR(8) |  |  |  |  |
| 47 | `PODORDLINORDERLINE` | CHAR(15) |  |  |  |  |
| 48 | `PODORDLINORDERSUBLINE` | DECIMAL(7,0) |  |  |  |  |
| 49 | `PODDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 50 | `PURORDERDELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 51 | `PRODUCTIONDEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 52 | `PRODUCTIONDEMANDCODE` | CHAR(15) |  |  |  |  |
| 53 | `ALLOCATIONCODE` | CHAR(15) |  |  |  |  |
| 54 | `ALLOCATIONLINENUMBER` | DECIMAL(5,0) |  |  |  |  |
| 55 | `ALLOCATIONCOMPONENTLINENUMBER` | DECIMAL(5,0) |  |  |  |  |
| 56 | `REPREQREQUISITIONTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 57 | `REPREQCODE` | CHAR(15) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CHOOSE,
       t.FORCEDWARNING,
       t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.HASERRORS,
       t.COMPANYCODE,
       t.ERRORMESSAGE,
       t.ENTITYTYPE,
       t.ENTITYDATE,
       t.ENTITYDESCRIPTION,
       t.ITEMTYPECOMPANYCODE
FROM   DB2ADMIN.WRKPROJECTLINKEDENTITY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

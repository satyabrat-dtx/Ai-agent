# DB2ADMIN.WRKPRODDEMANDPLANNINGCHECK

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 53
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 32796

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RECORDTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 1 | `ERRORLEVEL` | CHAR(5) |  |  |  |  |
| 2 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `PRODUCTIONDEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 4 | `PRODUCTIONDEMANDCODE` | CHAR(15) |  |  |  |  |
| 5 | `DLVSALORDLINESALORDCMYCODE` | CHAR(3) |  |  |  |  |
| 6 | `DLVSALORDLINESALORDCNTCODE` | CHAR(8) |  |  |  |  |
| 7 | `DLVSALORDERLINESALESORDERCODE` | CHAR(15) |  |  |  |  |
| 8 | `DLVSALESORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 9 | `DLVSALESORDERLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 10 | `DLVSALORDLINECMPORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 11 | `DELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 12 | `RESERVATIONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 13 | `RESERVATIONORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 14 | `RESERVATIONORDERCODE` | CHAR(15) |  |  |  |  |
| 15 | `RESERVATIONRESERVATIONLINE` | DECIMAL(7,0) |  |  |  |  |
| 16 | `INTDLVINTORDLINEINTORDCMYCODE` | CHAR(3) |  |  |  |  |
| 17 | `INTDLVINTORDLINEINTORDCNTCODE` | CHAR(8) |  |  |  |  |
| 18 | `INTDLVINTORDLINEINTORDERCODE` | CHAR(15) |  |  |  |  |
| 19 | `INTDLVINTORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 20 | `INTDLVINTORDLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 21 | `INTDELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 22 | `INTDOCINTDOCUMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 23 | `INTDOCINTDOCPRVCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 24 | `INTDOCINTDOCPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 25 | `INTDOCUMENTORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 26 | `INTDOCUMENTORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 27 | `ITEMDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 28 | `RESUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 29 | `RESUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 30 | `RESUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 31 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 32 | `AVAILABILITYWAREHOUSEGROUPCODE` | CHAR(3) |  |  |  |  |
| 33 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 34 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 35 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 36 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 37 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 38 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 39 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 40 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 41 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 42 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 43 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 44 | `PERIODSTARTDATE` | DATE |  |  |  |  |
| 45 | `PERIODENDDATE` | DATE |  |  |  |  |
| 46 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 47 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 48 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 49 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 50 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 51 | `AVLWAREHOUSEGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 52 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.RECORDTYPE,
       t.ERRORLEVEL,
       t.COMPANYCODE,
       t.PRODUCTIONDEMANDCOUNTERCODE,
       t.PRODUCTIONDEMANDCODE,
       t.DLVSALORDLINESALORDCMYCODE,
       t.DLVSALORDLINESALORDCNTCODE,
       t.DLVSALORDERLINESALESORDERCODE,
       t.DLVSALESORDERLINEORDERLINE,
       t.DLVSALESORDERLINEORDERSUBLINE,
       t.DLVSALORDLINECMPORDERLINE,
       t.DELIVERYDELIVERYLINE
FROM   DB2ADMIN.WRKPRODDEMANDPLANNINGCHECK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

# DB2ADMIN.ALLOCATIONIMPORT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 97
- **Primary key**: `COMPANYCODE`, `CODE`, `LINENUMBER`, `COMPONENTLINENUMBER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 36718

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `DELETEFLAG` | CHAR(1) |  |  |  |  |
| 4 | `STATUS` | CHAR(2) |  |  |  |  |
| 5 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 6 | `ALLOCATIONDATE` | DATE |  |  |  |  |
| 7 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 8 | `NOWCODE` | CHAR(15) |  |  |  |  |
| 9 | `LINENUMBER` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 10 | `COMPONENTLINENUMBER` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 11 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 12 | `EXPIRATIONDATE` | DATE |  |  |  |  |
| 13 | `THEORETICISSUEDATE` | DATE |  |  |  |  |
| 14 | `DETAILTYPE` | CHAR(1) |  |  |  |  |
| 15 | `ORIGINTYPE` | CHAR(2) |  |  |  |  |
| 16 | `DESTINATIONTYPE` | CHAR(2) |  |  |  |  |
| 17 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 18 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 19 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 20 | `DECOSUBCODE01` | CHAR(20) |  |  |  |  |
| 21 | `DECOSUBCODE02` | CHAR(10) |  |  |  |  |
| 22 | `DECOSUBCODE03` | CHAR(10) |  |  |  |  |
| 23 | `DECOSUBCODE04` | CHAR(10) |  |  |  |  |
| 24 | `DECOSUBCODE05` | CHAR(10) |  |  |  |  |
| 25 | `DECOSUBCODE06` | CHAR(10) |  |  |  |  |
| 26 | `DECOSUBCODE07` | CHAR(10) |  |  |  |  |
| 27 | `DECOSUBCODE08` | CHAR(10) |  |  |  |  |
| 28 | `DECOSUBCODE09` | CHAR(10) |  |  |  |  |
| 29 | `DECOSUBCODE10` | CHAR(10) |  |  |  |  |
| 30 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 31 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 32 | `PHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 33 | `WHSLOCATIONWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 34 | `WAREHOUSELOCATIONCODE` | CHAR(10) |  |  |  |  |
| 35 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 36 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 37 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 38 | `LOTCODE` | CHAR(35) |  |  |  |  |
| 39 | `ITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 40 | `ITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 41 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 42 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 43 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 44 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 45 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 46 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 47 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 48 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 49 | `WEIGHTUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 50 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 51 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 52 | `WEIGHTREALNET` | DECIMAL(15,5) |  |  |  |  |
| 53 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 54 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 55 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 56 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 57 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 58 | `ORDERCODE` | CHAR(15) |  |  |  |  |
| 59 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 60 | `ORDERSUBLINENUMBER` | DECIMAL(3,0) |  |  |  |  |
| 61 | `ORDERCOMPONENTLINENUMBER` | DECIMAL(3,0) |  |  |  |  |
| 62 | `DELIVERYLINENUMBER` | DECIMAL(3,0) |  |  |  |  |
| 63 | `RESERVATIONLINENUMBER` | DECIMAL(3,0) |  |  |  |  |
| 64 | `REPLENISHMENTREQUISITIONTMPCOD` | CHAR(3) |  |  |  |  |
| 65 | `REPLENISHMENTCODE` | CHAR(15) |  |  |  |  |
| 66 | `INTERNALGROUPINGNUMBER` | INTEGER | NOT NULL |  |  |  |
| 67 | `INTERNALGROUPINGLINENUMBER` | INTEGER | NOT NULL |  |  |  |
| 68 | `PICKINGCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 69 | `PICKINGCODE` | CHAR(15) |  |  |  |  |
| 70 | `ADUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 71 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 72 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 73 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 74 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 75 | `TEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 76 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 77 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 78 | `DECOCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 79 | `QUALITYLVLITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 80 | `PHYSICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 81 | `WHSLOCWHSZONEPHYWHSCMYCODE` | CHAR(3) |  |  |  |  |
| 82 | `CONTAINERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 83 | `CONTAINERELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 84 | `LOTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 85 | `ITEMELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 86 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 87 | `COUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 88 | `PICKINGCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 89 | `DERIVATIONCODE` | CHAR(15) |  |  |  |  |
| 90 | `DERIVATIONLINENUMBER` | DECIMAL(5,0) |  |  |  |  |
| 91 | `DERIVATIONCOMPONENTLINENUMBER` | DECIMAL(5,0) |  |  |  |  |
| 92 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 93 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 94 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 95 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 96 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ALLOCATIONIMPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.IMPORTSTATUS,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.DELETEFLAG,
       t.STATUS,
       t.COMPANYCODE,
       t.ALLOCATIONDATE,
       t.CODE,
       t.NOWCODE,
       t.LINENUMBER,
       t.COMPONENTLINENUMBER,
       t.TEMPLATECODE
FROM   DB2ADMIN.ALLOCATIONIMPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

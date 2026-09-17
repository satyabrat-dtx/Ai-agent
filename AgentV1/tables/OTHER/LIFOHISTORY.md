# DB2ADMIN.LIFOHISTORY

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 33
- **Primary key**: `COMPANYCODE`, `FISCALYEARYEAR`, `ITEMTYPECODE`, `SUBCODE01`, `SUBCODE02`, `SUBCODE03`, `SUBCODE04`, `SUBCODE05`, `SUBCODE06`, `SUBCODE07`, `SUBCODE08`, `SUBCODE09`, `SUBCODE10`, `ITEMLIFOGROUPCODE`, `WHSLIFOGRPSTDGROUPTYPECODE`, `WAREHOUSELIFOGROUPCODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 5287

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `FISCALYEARYEAR` | DECIMAL(4,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `SUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 4 | `SUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 5 | `SUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 6 | `SUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 7 | `SUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 8 | `SUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 9 | `SUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 10 | `SUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 11 | `SUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 12 | `SUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 13 | `ITEMLIFOGROUPCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 14 | `WHSLIFOGRPSTDGROUPTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 15 | `WAREHOUSELIFOGROUPCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 16 | `BASECOSTUNITCODE` | CHAR(3) |  | FK | foreign_key |  |
| 17 | `ENDYEARSTOCKONHAND` | DECIMAL(15,5) |  |  |  |  |
| 18 | `STOCKONHANDCHANGE` | DECIMAL(15,5) |  |  |  |  |
| 19 | `LIFOCOST` | DECIMAL(18,5) |  |  |  |  |
| 20 | `STOCKONHANDTOTALVALUE` | DECIMAL(18,5) |  |  |  |  |
| 21 | `DATATYPE` | CHAR(2) | NOT NULL |  |  |  |
| 22 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 23 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 24 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 25 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 26 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 27 | `ITEMLIFOGROUPCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 28 | `WHSLIFOGRPSTDGRPTYPECMYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 29 | `AVERAGELIFOCOST` | DECIMAL(18,5) |  |  |  |  |
| 30 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 31 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 32 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `LIFOHISTORY.COMPANYCODE = COMPANY.CODE` |
| `LIFOYEAR_FISCALYEAR` | `COMPANYCODE`, `FISCALYEARYEAR` | [`LIFOYEAR`](../OTHER/LIFOYEAR.md) | `COMPANYCODE`, `YEAR` | RESTRICT | `LIFOHISTORY.COMPANYCODE = LIFOYEAR.COMPANYCODE AND LIFOHISTORY.FISCALYEARYEAR = LIFOYEAR.YEAR` |
| `STANDARDGROUP_WAREHOUSELIFOGROUP` | `WHSLIFOGRPSTDGRPTYPECMYCODE`, `WHSLIFOGRPSTDGROUPTYPECODE`, `WAREHOUSELIFOGROUPCODE` | [`STANDARDGROUP`](../CORE_MASTER/STANDARDGROUP.md) | `STANDARDGROUPTYPECOMPANYCODE`, `STANDARDGROUPTYPECODE`, `CODE` | RESTRICT | `LIFOHISTORY.WHSLIFOGRPSTDGRPTYPECMYCODE = STANDARDGROUP.STANDARDGROUPTYPECOMPANYCODE AND LIFOHISTORY.WHSLIFOGRPSTDGROUPTYPECODE = STANDARDGROUP.STANDARDGROUPTYPECODE AND LIFOHISTORY.WAREHOUSELIFOGROUPCODE = STANDARDGROUP.CODE` |
| `UNITOFMEASURE_BASECOSTUNIT` | `BASECOSTUNITCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `LIFOHISTORY.BASECOSTUNITCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LIFOHISTORYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.FISCALYEARYEAR,
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
FROM   DB2ADMIN.LIFOHISTORY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

# DB2ADMIN.WRKOPPRODUCTIONPROGRESS

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 55
- **Primary key**: `COMPANYCODE`, `MACHINECODE`, `ITEMTYPECODE`, `QUALITYLEVELCODE`, `POSTINGDATE`, `PLANTCODE`, `WORKCENTERCODE`, `SHIFT`, `TEMPLATECODE`, `LOGICALWAREHOUSECODE`, `CREATIONUSER`, `CREATIONTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 131490

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `FINALSTEP` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `MACHINECODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `CHOOSE` | SMALLINT | NOT NULL |  |  |  |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 8 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 9 | `QUALITYLVLITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 10 | `QUALITYLEVELCODE` | DECIMAL(2,0) | NOT NULL | PK | primary_key |  |
| 11 | `POSTINGDATE` | DATE | NOT NULL | PK | primary_key |  |
| 12 | `PLANTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 13 | `PLANTCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 14 | `WORKCENTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 15 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 16 | `SHIFT` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 17 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 18 | `TEMPLATECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 19 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 20 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 21 | `CONTAINERELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 22 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 23 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 24 | `LOGICALWAREHOUSECODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 25 | `PHYSICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 26 | `PHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 27 | `ZONEPHYWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 28 | `ZONECODE` | CHAR(3) |  |  |  |  |
| 29 | `LOCWHSZONEPHYWHSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 30 | `LOCATIONCODE` | CHAR(10) |  |  |  |  |
| 31 | `LOTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 32 | `LOTITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 33 | `LOTSUBCODE01` | CHAR(20) |  |  |  |  |
| 34 | `LOTNUMBER` | CHAR(10) |  |  |  |  |
| 35 | `NOOFSPINDLES` | BIGINT | NOT NULL |  |  |  |
| 36 | `INITIALHANKREADING` | INTEGER | NOT NULL |  |  |  |
| 37 | `FINALHANKREADING` | INTEGER | NOT NULL |  |  |  |
| 38 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 39 | `PRODUCTION` | DECIMAL(15,5) |  |  |  |  |
| 40 | `DURATION` | DECIMAL(15,5) |  |  |  |  |
| 41 | `DOFF` | INTEGER | NOT NULL |  |  |  |
| 42 | `CREATIONUSER` | CHAR(50) | NOT NULL | PK | primary_key audit | User who created the row (audit). |
| 43 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 44 | `HANKUOMCODE` | CHAR(3) |  |  |  |  |
| 45 | `UOMCODE` | CHAR(3) |  |  |  |  |
| 46 | `SHOULDBEHANK` | DECIMAL(6,2) |  |  |  |  |
| 47 | `ACTUALCOUNT` | DECIMAL(11,4) |  |  |  |  |
| 48 | `COUNTCODE` | CHAR(4) |  |  |  |  |
| 49 | `EFFICIENCY` | DECIMAL(5,2) |  |  |  |  |
| 50 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 51 | `TEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 52 | `DOFFS` | INTEGER | NOT NULL |  |  |  |
| 53 | `DOFFMIN` | DECIMAL(4,2) |  |  |  |  |
| 54 | `WASTAGEQNTY` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKOPPRODUCTIONPROGRESSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.FINALSTEP,
       t.MACHINECODE,
       t.CHOOSE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.QUALITYLVLITEMTYPECOMPANYCODE,
       t.QUALITYLEVELCODE,
       t.POSTINGDATE
FROM   DB2ADMIN.WRKOPPRODUCTIONPROGRESS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

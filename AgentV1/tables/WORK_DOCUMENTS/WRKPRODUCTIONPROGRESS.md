# DB2ADMIN.WRKPRODUCTIONPROGRESS

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 35
- **Primary key**: `COMPANYCODE`, `MACHINECODE`, `ITEMTYPECODE`, `QUALITYLEVELCODE`, `POSTINGDATE`, `PLANTCODE`, `WORKCENTERCODE`, `SHIFT`, `TEMPLATECODE`, `LOGICALWAREHOUSECODE`, `CREATIONUSER`, `CREATIONTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 131692

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `FINALSTEP` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `MACHINECODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 7 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 8 | `QUALITYLVLITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 9 | `QUALITYLEVELCODE` | DECIMAL(2,0) | NOT NULL | PK | primary_key |  |
| 10 | `POSTINGDATE` | DATE | NOT NULL | PK | primary_key |  |
| 11 | `PLANTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 12 | `PLANTCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 13 | `WORKCENTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 14 | `SHIFT` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 15 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 16 | `TEMPLATECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 17 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 18 | `LOGICALWAREHOUSECODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 19 | `PHYSICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 20 | `PHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 21 | `ZONEPHYWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 22 | `ZONECODE` | CHAR(3) |  |  |  |  |
| 23 | `LOCWHSZONEPHYWHSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 24 | `LOCATIONCODE` | CHAR(10) |  |  |  |  |
| 25 | `LOTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 26 | `LOTITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 27 | `LOTSUBCODE01` | CHAR(20) |  |  |  |  |
| 28 | `LOTNUMBER` | CHAR(20) |  |  |  |  |
| 29 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 30 | `DURATION` | DECIMAL(15,5) |  |  |  |  |
| 31 | `CREATIONUSER` | CHAR(50) | NOT NULL | PK | primary_key audit | User who created the row (audit). |
| 32 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 33 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 34 | `TEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKPRODUCTIONPROGRESSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.FINALSTEP,
       t.MACHINECODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.QUALITYLVLITEMTYPECOMPANYCODE,
       t.QUALITYLEVELCODE,
       t.POSTINGDATE,
       t.PLANTCOMPANYCODE
FROM   DB2ADMIN.WRKPRODUCTIONPROGRESS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

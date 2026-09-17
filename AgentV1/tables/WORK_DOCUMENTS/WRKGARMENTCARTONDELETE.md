# DB2ADMIN.WRKGARMENTCARTONDELETE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `NUMBERID`, `CARTONITEMTYPECODE`, `CARTONSUBCODE01`, `CARTONCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 238513

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `CHOOSE` | SMALLINT | NOT NULL |  |  |  |
| 3 | `NUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 4 | `CARTONITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `CARTONSUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 6 | `CARTONCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 7 | `SALESORDERCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 8 | `SALESORDERCODE` | CHAR(15) | NOT NULL |  |  |  |
| 9 | `PACKINGGROUP` | CHAR(15) |  |  |  |  |
| 10 | `PACKINGGROUPDESCRIPTION` | CHAR(200) |  |  |  |  |
| 11 | `CARTONQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 12 | `NOOFCARTONS` | DECIMAL(11,0) |  |  |  |  |
| 13 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 14 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 15 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKGARMENTCARTONDELETEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.CHOOSE,
       t.NUMBERID,
       t.CARTONITEMTYPECODE,
       t.CARTONSUBCODE01,
       t.CARTONCODE,
       t.SALESORDERCOUNTERCODE,
       t.SALESORDERCODE,
       t.PACKINGGROUP,
       t.PACKINGGROUPDESCRIPTION,
       t.CARTONQUANTITY
FROM   DB2ADMIN.WRKGARMENTCARTONDELETE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```

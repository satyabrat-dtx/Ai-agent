# DB2ADMIN.CSMINTERFACECONTROL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `ITEMTYPECODE`, `LOGICALWAREHOUSECODE`, `STOCKTRANSACTIONTEMPLATECODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 135256

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EVENTCODE` | CHAR(15) |  | FK | foreign_key |  |
| 2 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 3 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 6 | `LOGICALWAREHOUSECODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 7 | `STOCKTRNTEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 8 | `STOCKTRANSACTIONTEMPLATECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 9 | `EFFECTIVEFROMDATE` | DATE | NOT NULL |  |  |  |
| 10 | `EFFECTIVETODATE` | DATE |  |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `CSMINTERFACECONTROL.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CSMINTERFACECONTROL.COMPANYCODE = DIVISION.COMPANYCODE AND CSMINTERFACECONTROL.DIVISIONCODE = DIVISION.CODE` |
| `EVENTMASTER_EVENT` | `EVENTCODE` | [`EVENTMASTER`](../CORE_MASTER/EVENTMASTER.md) | `CODE` | RESTRICT | `CSMINTERFACECONTROL.EVENTCODE = EVENTMASTER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CSMINTERFACECONTROLUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EVENTCODE,
       t.DIVISIONCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.LOGICALWAREHOUSECOMPANYCODE,
       t.LOGICALWAREHOUSECODE,
       t.STOCKTRNTEMPLATECOMPANYCODE,
       t.STOCKTRANSACTIONTEMPLATECODE,
       t.EFFECTIVEFROMDATE,
       t.EFFECTIVETODATE,
       t.CREATIONDATETIME
FROM   DB2ADMIN.CSMINTERFACECONTROL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
